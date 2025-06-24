import tweepy

# Step 1: Set up Twitter API authentication
consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_token_secret = 'token'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Step 2: Define a function to scrape 50 replies
def get_replies(query, max_tweets=50):
    replies = []
    for tweet in tweepy.Cursor(api.search_tweets, 
                               q=query,
                               result_type="recent",  # Get the most recent tweets
                               tweet_mode='extended',  # Get the full tweet text
                               lang="en").items(max_tweets):
        if hasattr(tweet, 'in_reply_to_status_id_str') and tweet.in_reply_to_status_id_str is not None:
            replies.append({
                'tweet_id': tweet.id_str,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name,
                'text': tweet.full_text,
                'in_reply_to': tweet.in_reply_to_status_id_str,
                'in_reply_to_user': tweet.in_reply_to_user_id_str
            })
    return replies

# Step 3: Use the function to get replies
query = "YOUR_SEARCH_QUERY"  # For example, a hashtag or specific keyword you're interested in
replies = get_replies(query, max_tweets=50)

# Step 4: Print the replies or save them to a file
for reply in replies:
    print(f"User: {reply['user']}")
    print(f"Tweet: {reply['text']}")
    print(f"Created At: {reply['created_at']}")
    print(f"Reply to Tweet ID: {reply['in_reply_to']}")
    print(f"Reply to User ID: {reply['in_reply_to_user']}")
    print("-" * 80)