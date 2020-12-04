
import twitter_api


fetched_tweets_filename = "tweets.txt"

def test_empty():
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, [])
    assert len(fetched_tweets_filename) == 0


if __name__ == '__main__':
    pytest.main("test_twitter_api.py")
