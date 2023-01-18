import tweepy


class TwitterAPI:
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret
    ):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(
            self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
        )

    def post_tweet(self, tweet, media_ids=[]):
        self.api.update_status(status=tweet, media_ids=media_ids)
        print("Tweet posted successfully!")

    def reply_tweet(self, tweet, status_id, media_ids=[]):
        self.api.update_status(
            status=tweet, in_reply_to_status_id=status_id, media_ids=media_ids
        )
        print("Reply tweet posted successfully!")

    def get_tweet(self, tweet_id):
        tweet = self.api.get_status(tweet_id)
        return tweet

    def delete_tweet(self, tweet_id):
        self.api.destroy_status(tweet_id)
        print("Tweet deleted successfully!")

    def get_user_timeline(self, screen_name, count):
        tweets = self.api.user_timeline(screen_name=screen_name, count=count)
        return tweets

    def get_mentions(self, count):
        tweets = self.api.mentions_timeline(count=count)
        return tweets

    def get_home_timeline(self, count):
        tweets = self.api.home_timeline(count=count)
        return tweets

    def search_tweets(self, query, count):
        tweets = self.api.search(q=query, count=count)
        return tweets

    def favorite_tweet(self, tweet_id):
        self.api.create_favorite(tweet_id)
        print("Tweet favorited successfully!")

    def unfavorite_tweet(self, tweet_id):
        self.api.destroy_favorite(tweet_id)
        print("Tweet unfavorited successfully!")

    def follow_user(self, screen_name):
        self.api.create_friendship(screen_name)
        print("Now following", screen_name)

    def unfollow_user(self, screen_name):
        self.api.destroy_friendship(screen_name)
        print("No longer following", screen_name)

    def upload_media(self, file_path):
        media_id = self.api.media_upload(file_path).media_id_string
        return media_id
