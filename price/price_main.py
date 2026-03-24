from price_fetch import get_real_time_price
from price_move_sig import price_move
from utils.logger import get_logger

logger = get_logger(__name__)
def main():
    try:
        logger.info("Start testing price_fech and price_main")
    