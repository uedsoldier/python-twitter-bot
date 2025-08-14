import sys, os

ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from twitter_bot.twitter_bot import TwitterBot

bot = TwitterBot()

print('Test Event Tracker')
print('Days since start:', bot.event_tracker.compute_days_since_start())