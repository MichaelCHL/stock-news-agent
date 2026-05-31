import pytest
from utils.rate_limiter import rate_limit
from collections import defaultdict

@pytest.mark.parametrize('user_id, active_user_data, current_time, result', [
    ('user_1', {'user_3': [10]}, 15, False),
    ('user_1', {'user_1': [10], 'user_3': [11]}, 12, False),
    ('user_1', {'user_1': [10, 12], 'user_3': [11]}, 15, True),
    ('user_1', {'user_1': [10, 12, 14], 'user_3': [11]}, 75, False)


])

def test_rate_limit(user_id: str, active_user_data: dict, current_time: float, result: bool):
    active_users = defaultdict(list, active_user_data)
    assert rate_limit(user_id, active_users, current_time) == result