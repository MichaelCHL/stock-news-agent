from fastapi import FastAPI, Request, HTTPException
from linebot.v3.messaging import AsyncApiClient, AsyncMessagingApi, Configuration, ReplyMessageRequest, TextMessage
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.webhook import WebhookParser
from orchestrator import orchestrator
from price.ticker_search import ticker_search
from config import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN
from utils.logger import get_logger
from collections import defaultdict

import time

config = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

logger = get_logger(__name__)
app = FastAPI()
async_api_client = AsyncApiClient(config)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(LINE_CHANNEL_SECRET)
active_users = defaultdict(list)

@app.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
        logger.info(events)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessageContent):
            continue
        current_time = time.time()
        user_id = event.source.user_id
        active_users[user_id].append(current_time)
        # rate limit: 2 times allowance within 60 seconds window 
        while active_users[user_id] and current_time - active_users[user_id][0] > 60:
            active_users[user_id].pop(0)
        if len(active_users[user_id]) > 2:
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="You've hit the rate limit (2 requests per 60 seconds). Please try again later.")]
                )
            )
            continue

        user_input = ticker_search(event.message.text)
        if not user_input:
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Failed to find the ticker. Please try another one.")]
                )
            )
            continue 

        ticker_symbol = user_input.upper()
        
        result = await orchestrator(ticker_symbol)
        if not result:
            result = f"Sorry, I couldn't retrieve news for {ticker_symbol}. Please try again."
        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=result)]
            )
        )

    return 'OK'