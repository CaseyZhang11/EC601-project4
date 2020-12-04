
import twitter_api

weibo_client = weibo_api.init()

fetched_tweets_filename = "tweets.txt"

def test_empty():
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, [])
    assert len(fetched_tweets_filename) == 0


if __name__ == '__main__':
    pytest.main("test_weibo_api.py")
