import pytest
from unittest.mock import AsyncMock, patch
from orchestrator import orchestrator


@patch("orchestrator.search", new_callable=AsyncMock) # controls the first param
@patch("orchestrator.get_real_time_price", new_callable=AsyncMock) # controls the second param
async def test_orchestrator(mock_get_real_time_price, mock_search):
    mock_get_real_time_price.return_value = {
    'SPY': {'percent_change': 0},
    'AMD': {'percent_change': 3},
}
    mock_search.return_value = "AMD just secured a deal with Google that leads to a leap in their stock price"
    result = await orchestrator('AMD')

    assert result == mock_search.return_value

@patch("orchestrator.get_real_time_price", new_callable=AsyncMock)
async def test_orchestrator_none(mock_get_real_time_price):
    mock_get_real_time_price.return_value = None
    result = await orchestrator('NVDA')
    
    assert result is None