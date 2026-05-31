from price.price_fetch import get_real_time_price
from price.price_move_sig import price_move
from agent.web_search import search
from utils.logger import get_logger

logger = get_logger(__name__)

async def orchestrator(ticker: str):
    today_price = await get_real_time_price(ticker)
    if not today_price:
        logger.error("Failed to fetch data!")
        return

    spy_pc = today_price.get("SPY").get("percent_change")
    ticker_pc = today_price.get(f"{ticker}").get("percent_change")
    ticker_performance = price_move(ticker_pc, spy_pc)
    if ticker_performance in ["market_wild_drop", "underperform", "underperform_mild", "outperform_mild", "outperform", "outperform_wild", "underperform_wild"]:
        try:
            news = await search(ticker.upper())
            return news
        except Exception as e:
            logger.error(e)
            return
        
    elif ticker_performance == 'market_surge':
        logger.info("Market is promising today!")
    elif ticker_performance == 'neutral':
        logger.info("It's a steady day")
    else:
        logger.info("No coditional is met, there's an uncatched condition")

