import sys
import os

ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from twitter_bot.twitter_bot import TwitterBot
from twitter_bot.responses import UserResponse

bot = TwitterBot()
user_response: UserResponse = bot.twitter_client.get_me()
if(user_response.success):
    print(f'Username: {user_response.user_data}')
else:
    print(f'Error: {user_response.error}')