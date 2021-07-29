from config import REDIS_HOST, REDIS_PORT
import redis

class Cache:
    def __init__(self):
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    def cache(self):
        return self.r
