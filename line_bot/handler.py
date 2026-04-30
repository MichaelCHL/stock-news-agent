from fastapi import FastAPI, Request, HTTPException
from linebot.v3.messaging import AsyncApiClient, AsyncMessagingApi, Configuration, ReplyMessageRequest, TextMessage
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.webhook import WebhookParser
from orchestrator import orchestrator
from price.ticker_search import ticker_search
from config import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN

config = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

app = FastAPI()
async_api_client = AsyncApiClient(config)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(LINE_CHANNEL_SECRET)

@app.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessageContent):
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
        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=result)]
            )
        )

    return 'OK'