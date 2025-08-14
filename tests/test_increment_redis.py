import redis
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_CONTAINER_PORT = int(os.getenv('REDIS_CONTAINER_PORT','6379'))
REDIS_ADMIN_USER = os.getenv('REDIS_ADMIN_USER', 'default')
REDIS_ADMIN_PASSWORD = os.getenv('REDIS_ADMIN_PASSWORD', '')

r = redis.Redis(host=REDIS_HOST, port=REDIS_CONTAINER_PORT, username=REDIS_ADMIN_USER,password=REDIS_ADMIN_PASSWORD,decode_responses=True)

test_counter = int(r.get('test_counter'))

print(f'Test counter value: {test_counter}')

test_counter += 1
r.set('test_counter', test_counter)

print(f'Test counter value (after increment): {test_counter}')



