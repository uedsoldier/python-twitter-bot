from twitter_bot.twitter_bot import TwitterBot
from redis.exceptions import RedisError, ConnectionError, TimeoutError, AuthenticationError, ResponseError

if __name__ == "__main__":
    try:
        bot = TwitterBot()
        bot.run()
    except RedisError as redis_e:
        print(f'Redis error: {redis_e}')