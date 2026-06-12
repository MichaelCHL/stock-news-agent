import pytest
from price.ticker_search import ticker_search
from unittest.mock import patch

@pytest.mark.parametrize('name, result', [
    ('2330.TW', '2330.TW'),
    ('MICHAEL JORDAN IS THE GOAT HANDS DOWN', None),
    ('NVDA', 'NVDA')
])
def test_ticker_search(name: str, result: str):
    ticker = ticker_search(name)
    assert ticker == result

@patch("price.ticker_search.finnhub_client")
def test_ticker_search_api(mock_finnhub_client):
    mock_finnhub_client.symbol_lookup.return_value = {"result": [{"symbol": "APPL"}, {"symbol": "APPL."}]}
    result_appl = ticker_search('apple')
    
    mock_finnhub_client.symbol_lookup.return_value = {"result": [{"symbol": "2330.TW"}, {"symbol": "2330"}]}
    result_tsmc = ticker_search('台積電')

    mock_finnhub_client.symbol_lookup.return_value = {"result": []}
    result_false = ticker_search('台雞電')


    assert result_appl == 'APPL'
    assert result_tsmc == '2330.TW'
    assert result_false == None