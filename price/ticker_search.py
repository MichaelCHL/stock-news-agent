import finnhub
from config import FINNHUB_API_KEY

finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

def ticker_search(name: str):
    if len(name) >= 30:
        return None
    if any('\u4e00' <= char <= '\u9fff' for char in name):
        results = finnhub_client.symbol_lookup(name).get("result")
        for result in results:
            if '.' not in result.get("symbol"):
                return result.get("symbol")
        return None
    elif ' ' not in name and name.isupper():
        return name
    elif any(char.isdigit() for char in name) or '.' in name:
        return name
    else:
        results = finnhub_client.symbol_lookup(name).get("result")
        for result in results:
            if '.' not in result.get("symbol"):
                return result.get("symbol")
        return None