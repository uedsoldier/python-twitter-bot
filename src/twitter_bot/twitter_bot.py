from twitter_bot.phrase_manager import PhraseManager
from twitter_bot.twitter_client import TwitterClient
from twitter_bot.event_tracker import EventTracker
from twitter_bot.log_manager import LogManager
from twitter_bot.responses import TweetResponse
from tweepy import TooManyRequests, Unauthorized

import time
import logging 

from redis import Redis

from twitter_bot.config import (
    REDIS_HOST, REDIS_CONTAINER_PORT, REDIS_ADMIN_USER, REDIS_ADMIN_PASSWORD,
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)

class TwitterBot:

    def __init__(self, redis_db_number: int = 0):
        self.logger = LogManager.get_logger(__name__, level=logging.DEBUG)
        self.redis_store = Redis(
                host=REDIS_HOST,
                port=REDIS_CONTAINER_PORT,
                username=REDIS_ADMIN_USER,
                password=REDIS_ADMIN_PASSWORD,
                decode_responses=True,
                db=redis_db_number
            )
        self.phrase_manager = PhraseManager(self.redis_store)
        self.twitter_client = TwitterClient(
            TWITTER_ACCESS_TOKEN=TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_TOKEN_SECRET=TWITTER_ACCESS_TOKEN_SECRET,
            TWITTER_CONSUMER_KEY=TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET=TWITTER_CONSUMER_SECRET,
        )
        self.event_tracker = EventTracker(self.redis_store)

    def run(self): 
        days = self.event_tracker.compute_days_since_start()
        raw_twitt = self.phrase_manager.generate_raw_phrase()
        twitt = self.phrase_manager.format_raw_phrase(raw_twitt,days)
        twitt_with_hashtags = twitt + self.phrase_manager.hashtag
        self.logger.info(f'Generated tweet message: {twitt_with_hashtags}')

        try:
            response: TweetResponse = self.twitter_client.publish_tweet(twitt_with_hashtags)
            if response.success:
                self.phrase_manager.add_raw_phrase_to_used(raw_twitt)
                self.logger.info(f'Added raw phrase to used phrases: {raw_twitt}')
                self.logger.info(f'Published tweet: {response.url}')
            else:
                self.logger.error(f'Error publishing tweet: {response.error} (Status code: {response.status_code})')
        except TooManyRequests as e:
            reset_timestamp = int(e.response.headers.get('x-rate-limit-reset', 0))
            wait_minutes: int = int((reset_timestamp - time.time()) / 60)
            self.logger.warning(f'Rate limit exceeded. Try again in {wait_minutes} minutes.')
        
        except Unauthorized as e:
            self.logger.error(f'Invalid Twitter API credentials: {e}')

        except Exception as e:
            self.logger.error(f'An unexpected error occurred: {e}')
            
        
        

       
       
