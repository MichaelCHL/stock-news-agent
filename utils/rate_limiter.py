from config import RATE_LIMIT, TIME_THRESHOLD

def rate_limit(user_id: str, active_users: dict, current_time: float) -> bool:
    if user_id not in active_users:
        active_users[user_id].append(current_time)
        return False
    
    active_users[user_id].append(current_time)

    while active_users[user_id] and current_time - active_users[user_id][0] > TIME_THRESHOLD:
        active_users[user_id].pop(0)
    if len(active_users[user_id]) > RATE_LIMIT:
        return True
    
    return False
    

    
    
    