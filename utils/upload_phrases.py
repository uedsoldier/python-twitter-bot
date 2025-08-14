import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, ruta_src)

from twitter_bot.phrase_manager import PhraseManager
import redis
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_CONTAINER_PORT = int(os.getenv('REDIS_CONTAINER_PORT','6379'))
REDIS_ADMIN_USER = os.getenv('REDIS_ADMIN_USER', 'default')
REDIS_ADMIN_PASSWORD = os.getenv('REDIS_ADMIN_PASSWORD', '')

r = redis.Redis(host=REDIS_HOST, port=REDIS_CONTAINER_PORT, username=REDIS_ADMIN_USER,password=REDIS_ADMIN_PASSWORD,decode_responses=True)

phrases_to_load = [

]

pm = PhraseManager(redis_store=r)

pm.load_phrases(phrases_to_load)
