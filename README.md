# Stock News Agent

## Overview
This is a stock agent that receives ticker symbol or company name from the user via LINE app and provides the latest news that cause the stock price to surge or fail.

## Tech Stack
- Python 3.12
- FastAPI
- Anthropic API
- Finnhub API
- LINE Messaging API
- httpx
- Streamlit
- Railway
- uv

## How to run it locally 
1. Clone the project
```
git clone https://github.com/MichaelCHL/stock-news-agent.git
```

2. Install dependencies
```
uv sync
```

3. Copy .env.example to .env and fill in the values for API keys.

4. Starting the server
To run locally:
- start uvicorn
- start ngrok
- set webhook URL to ngrok URL
```
uvicorn line_bot.handler:app --reload  --port 8000
ngrok http 8000

```

To deploy to Railway:
- Push to GitHub
- Set environment variables in Railway dashboard
- Set webhook URL to Railway URL

## Environment variables
Create a .env file in the project root with following values: 
```
FINNHUB_API_KEY = ""
ANTHROPIC_API_KEY = ""
LINE_CHANNEL_SECRET = ""
LINE_CHANNEL_ACCESS_TOKEN = ""
```

## Project structure
```
project-root/
├── agent/
|   └── web_search.py # Anthropic API news search
├── line_bot
|   └── handler.py # LINE API webhook
├── price/
|   ├── price_fetch.py # Finnhub stock price API
|   ├── price_main.py # Main file for price folder function testing
|   ├── price_move_sig.py # Stock movement checker
|   └── ticker_search.py # ticker searcher & converter
├── utils
|   └── logger.py # logger settings
├── app.py
├── config.py
├── orchestrator.py
├── README.md
├── uv.lock
└──.env.example 
```