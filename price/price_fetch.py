from utils.logger import get_logger
from typing import Dict, Optional
from config import FINNHUB_API_KEY

import httpx

logger = get_logger(__name__)

async def get_real_time_price(symbol: str) -> Optional[Dict[str, Dict[str,float]]]:
    try:
        logger.info("Initiate API Request to FinnHub...") 
        async with httpx.AsyncClient() as client:
            spy = await client.get(f"https://finnhub.io/api/v1/quote?symbol=SPY&token={FINNHUB_API_KEY}")
            selected = await client.get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}")

        spy_current = spy.json()["c"]
        spy_pc = spy.json()["dp"]
        select_current = selected.json()["c"]
        select_pc = selected.json()["dp"]
        logger.info(f"Successfully retrieved price change percentage for SPY and {symbol}")
        return {
                "SPY": {"current_price": spy_current, "percent_change": spy_pc},
                f"{symbol}": {"current_price": select_current, "percent_change": select_pc}
                }
    except httpx.RequestError as e:
        logger.exception(f"Request error: {e}") 
        return None
    except httpx.HTTPStatusError as e:
        logger.exception(f"HTTP Status error: {e}") 
        return None      
    except KeyError as e:
        logger.exception(f"Missing expected key in API response {e}")
        return None

