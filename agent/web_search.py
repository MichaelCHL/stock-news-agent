import anthropic
from utils.logger import get_logger
from datetime import datetime
from config import MODEL, MAX_TOKENS

logger =  get_logger(__name__)

async def search(ticker):
    today_dt = datetime.now().strftime("%Y-%m-%d")

    try:
        logger.info("Initiating a client...")
        client = anthropic.AsyncAnthropic()

        response = await client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": f"Search for the top 3 news stories about {ticker} on {today_dt} that explain why the stock price moved significantly today. Be concise and specific",
                }
            ],
            tools=[{"type": "web_search_20260209", 
                    "name": "web_search",
                    "max_uses": 1
                    }]
        )


        summary = []
        for block in response.content:
            if block.type == 'text':
                summary.append(block.text)
        result = ''.join(summary)
        
        logger.info("Result retrieved successfully!")
        return result
    
    except Exception as e:
        logger.error(f"Failed to retreive the latest news related to {ticker} on {today_dt}")

if __name__ == '__main__':
    search('NVDA')
