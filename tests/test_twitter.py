import sys
import os

from twitter_bot.twitter_bot import TwitterBot
from twitter_bot.responses import UserResponse

bot = TwitterBot()
user_response: UserResponse = bot.twitter_client.get_me()
if(user_response.success):
    print(f'Username: {user_response.user_data}')
else:
    print(f'Error: {user_response.error}')