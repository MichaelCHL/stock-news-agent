from dotenv import load_dotenv
from utils.logger import get_logger
from finnhub.exceptions import FinnhubAPIException
from typing import Dict, Optional

import finnhub
import os

load_dotenv()
logger = get_logger(__name__)
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

def get_real_time_price(symbol: str) -> Optional[Dict[str, Dict[str,float]]]:
    try:
        logger.info("Initiate API Request to FinnHub...") 
        spy = finnhub_client.quote(symbol='SPY')
        selected = finnhub_client.quote(symbol=symbol)

        spy_current = spy["c"]
        spy_pc = spy["dp"]
        select_current = selected["c"]
        select_pc = selected["dp"]
        logger.info(f"Successfully retrieved price change percentage for SPY and {symbol}")
        return {
                "SPY": {"current_price": spy_current, "percent_change": spy_pc},
                f"{symbol}": {"current_price": select_current, "percent_change": select_pc}
                }
    except FinnhubAPIException as e:
        logger.exception(f"API error: {e}") 
        return None


