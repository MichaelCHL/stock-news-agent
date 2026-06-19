import pytest
import httpx
from unittest.mock import patch, AsyncMock
from price.price_fetch import get_real_time_price

@patch("price.price_fetch.httpx.AsyncClient")
async def test_get_real_time_price(mock_async_client):
    mock_client_instance = AsyncMock()
    mock_client_instance.get.side_effect = [AsyncMock(json=lambda: {"c": 680.99, "dp": 10.2}),
                                            AsyncMock(json=lambda: {"c": 264.11, "dp": 1.2})]

    mock_async_client.return_value.__aenter__.return_value = mock_client_instance
    result_AMD = await get_real_time_price('AMD')
    # print(result_AMD)
    assert result_AMD == {
    "SPY": {"current_price": 680.99, "percent_change": 10.2},
    "AMD": {"current_price": 264.11, "percent_change": 1.2}
}


@patch("price.price_fetch.httpx.AsyncClient")
async def test_get_real_time_price_fail(mock_async_client):
    mock_client_instance = AsyncMock()
    mock_client_instance.get.side_effect = httpx.RequestError("Connection failed") 
    mock_async_client.return_value.__aenter__.return_value = mock_client_instance
    result_fail = await get_real_time_price("NVDA")
    assert result_fail == None 