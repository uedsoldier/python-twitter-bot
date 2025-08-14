from datetime import datetime
from redis import Redis

class EventTracker:
    def __init__(self, redis_store: Redis, key_start_date='initial_date'):
        self.store = redis_store
        self.key_start_date = key_start_date

    def compute_days_since_start(self):
        start_date = self.store.get(self.key_start_date)
        if not start_date:
            return 0
        last_date = datetime.strptime(start_date, '%Y-%m-%d')
        return (datetime.today() - last_date).days
