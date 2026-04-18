from price.price_fetch import get_real_time_price
from price.price_move_sig import price_move
from agent.web_search import search
from utils.logger import get_logger

import anthropic

logger = get_logger(__name__)

def orchestrator(ticker):
    # ticker = input("Please enter a ticker symbol")
    today_price = get_real_time_price(ticker)
    if not today_price:
        logger.error("Failed to fetch data!")
        return

    spy_pc = today_price.get("SPY").get("percent_change")
    ticker_pc = today_price.get(f"{ticker}").get("percent_change")
    ticker_performance = price_move(ticker_pc, spy_pc)
    if ticker_performance in ["market_wide_drop", "underperform", "underperform_mild", "outperform_mild", "outperform"]:
        try:
            news = search(ticker)
            return news
        except anthropic.APIConnectionError as e:
            print("API Connection Failed!")
            logger.error(e)
            return
        
    elif ticker_performance == 'market_surge':
        print("Market is promising today!")
    elif ticker_performance == 'neutral':
        print("It's a steady day")
    else:
        print("No coditional is met, there's an uncatched condition")
if __name__ == "__main__":
    main()
