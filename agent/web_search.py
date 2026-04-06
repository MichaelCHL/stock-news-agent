import os
import anthropic

from dotenv import load_dotenv
from config import MODEL, MAX_TOKENS

load_dotenv()

def search(ticker):
    client = anthropic.Anthropic()

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {
                "role": "user",
                "content": f"Search for news related to {ticker} that causes the price change",
            }
        ],
        tools=[{"type": "web_search_20260209", "name": "web_search"}]
    )

    return response
