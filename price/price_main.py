from price.price_fetch import get_real_time_price
from price.price_move_sig import price_move
from utils.logger import get_logger

logger = get_logger(__name__)
def main(ticker):
    logger.info("Start testing price_fech and price_main")
    try:
        logger.info("Testing get_real_time_price..")
        prices = get_real_time_price(ticker)
        ticker_pc = prices[f"{ticker}"]["percent_change"]
        spy_pc = prices['SPY']["percent_change"]
        logger.info("get_real_time_price passed!")
    except TypeError as e:
        logger.exception(f"Unable to get the percent change: {e}")
        print("Something's wrong with get_real_time_price!")
        return
    
    try:
        logger.info("Testing price_move..")
        result = price_move(ticker_pc, spy_pc)
        print(result)
        logger.info("price_move passed!")
    except KeyError as e:
        logger.exception(f"Unable to find the given ticker price:", e)
        print("Something's wrong with price_move!")

if __name__ == '__main__':
    main('ONDS')