import tweepy
from twitter_bot.responses import TweetResponse, UserResponse


class TwitterClient:
    def __init__(self, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET):
        self.client = tweepy.Client(
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )
    
    def get_me(self):
        try:
            response = self.client.get_me()
            return UserResponse(
                success=True,
                user_data=response.data,
            )
        except tweepy.TooManyRequests as e:
            return UserResponse(
                success=False,
                error='Too many requests',
                status_code=429
            )
        except tweepy.Unauthorized as e:
            return UserResponse(
                success=False,
                error='Unauthorized',
                status_code=401
            )
        except Exception as e:
            return UserResponse(
                success=False,
                error=str(e),
                status_code=500
            )

    def publish_tweet(self, tweet):
        try:
            response = self.client.create_tweet(text=tweet)
            url = f'https://twitter.com/user/status/{response.data["id"]}'
            return TweetResponse(
                success=True,
                url=url,
            )
        except tweepy.TooManyRequests as e:
            return TweetResponse(
                success=False,
                error='Too many requests',
                status_code=429
            )
        except tweepy.Unauthorized as e:
            return TweetResponse(
                success=False,
                error='Unauthorized',
                status_code=401
            )
        except Exception as e:
            return TweetResponse(
                success=False,
                error=str(e),
                status_code=500
            )
