import sys
import os

from twitter_bot.twitter_bot import TwitterBot

bot = TwitterBot()

days_since = bot.event_tracker.compute_days_since_start()
forced_phrase = bot.phrase_manager.get_forced_phrase(remove_forced_phrase=False)
normal_phrase = bot.phrase_manager.get_phrase(add_phrase_to_used=False)

print(f'Forced phrase: {forced_phrase}')
print(f'Normal phrase: {normal_phrase}')
