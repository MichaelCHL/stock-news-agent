from price_fetch import get_real_time_price
from price_move_sig import price_move
from utils.logger import get_logger

logger = get_logger(__name__)
def main():
    logger.info("Start testing price_fech and price_main")
    try:
        logger.info("Testing get_real_time_price..")
        get_real_time_price('ONDS')
        logger.info("get_real_time_price passed!")
    except:
        logger.error("Something's wrong with get_real_time_price!")
    
    try:
        logger.info("Testing price_move..")
        price_move()
        logger.info("price_move passed!")
    except:
        logger.error("Something's wrong with price_move!")

if __name__ == '__main__':
    main()