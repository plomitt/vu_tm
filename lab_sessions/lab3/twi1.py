import tweepy
import json
import os

# Your Bearer Token from Twitter API v2
BEARER_TOKEN = "token"

# Number of tweets to fetch
N = 50

# Output filename
OUTPUT_FILE = "my_tweets1.json"

# Authenticate
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# Search query for replies (not original tweets)
query = 'is:reply -is:retweet a lang:en'  # English replies only

# Fields to fetch
tweet_fields = ['conversation_id', 'created_at', 'author_id']
expansions = ['in_reply_to_user_id']

# Fetch tweets
tweets_data = {}
count = 0

for tweet in tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=tweet_fields,
    expansions=expansions,
    max_results=100  # max per request
):
    for tweet_obj in tweet.data:
        if count >= N:
            break

        tweet_text = tweet_obj.text
        tweet_id = tweet_obj.id
        tweet_url = f"https://twitter.com/i/web/status/{tweet_id}"

        tweets_data[str(count + 1)] = {
            "sentiment_label": "",
            "text_of_tweet": tweet_text,
            "tweet_url": tweet_url
        }
        count += 1

    if count >= N:
        break

# Fill remaining slots (if not enough tweets found)
for i in range(count + 1, N + 1):
    tweets_data[str(i)] = {
        "sentiment_label": "",
        "text_of_tweet": "",
        "tweet_url": ""
    }

# Save to JSON file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(tweets_data, f, indent=4, ensure_ascii=False)

print(f"{len(tweets_data)} tweets saved to {OUTPUT_FILE}")
