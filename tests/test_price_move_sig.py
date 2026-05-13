import pytest
from price.price_move_sig import price_move

@pytest.mark.parametrize('ticker_pc, spy_pc, result', [
    (3, 3, "market_surge"), 
    (3, 0, "outperform"),
    (3, -3, "outperform_wild"),
    (0, 3, "underperform"),
    (0, 0, "neutral"),
    (0, -3, "market_wild_drop"),
    (-3, 3, "underperform_wild"),
    (-3, 0, "underperform"),
    (-3, -3, "market_wild_drop")
    ])
def test_price_move(ticker_pc: int, spy_pc: int, result: str):
    assert price_move(ticker_pc, spy_pc) == result