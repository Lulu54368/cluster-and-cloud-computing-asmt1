import json
from datetime import datetime
from collections import defaultdict

# Open tweets file
with open("twitter-50mb.json", 'r') as file:
    data = json.load(file)

sentiments_by_day = defaultdict(float)
sentiments_by_hour = defaultdict(float)
sentiments_by_day_count = defaultdict(float)
sentiments_by_hour_count = defaultdict(float)

total_tweet_hour = defaultdict(int)
total_tweet_day = defaultdict(int)

for tweet in data['rows']:
    # check if there is empty row
    if tweet.get('doc') is not None:
        created_at = tweet['doc']['data']['created_at']

        # Convert created_at to a datetime object and extract the hour
        # "created_at":"2021-06-21T03:21:05.000Z"
        parsed_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        month_day_key = parsed_date.strftime("%m-%d")
        month_day_hour_key = parsed_date.strftime("%m-%d-%H")
        
        # Check if this tweet has 'sentiment' attribute
        sentiment = tweet['doc']['data'].get('sentiment')
        
        # Count busiest hour
        total_tweet_hour[month_day_hour_key] += 1
        
        # Count busiest day
        total_tweet_day[month_day_key] += 1
        
        if sentiment is None:
            continue
        # Check if the "sentiment" attribute is float or dict
        elif isinstance(sentiment, dict):
            sentiment_score = tweet['doc']['data']['sentiment']['score']
            
            if sentiment_score != 0:
                # Count happist hour
                sentiments_by_hour[month_day_hour_key] += sentiment_score
                sentiments_by_hour_count[month_day_hour_key] += 1

                # Count happist day
                sentiments_by_day[month_day_key] += sentiment_score
                sentiments_by_day_count[month_day_key] += 1
        else:
            sentiment_score = tweet['doc']['data']['sentiment']
            
            if sentiment_score != 0:
                # Count happist hour
                sentiments_by_hour[month_day_hour_key] += sentiment_score
                sentiments_by_hour_count[month_day_hour_key] += 1

                # Count happist day
                sentiments_by_day[month_day_key] += sentiment_score
                sentiments_by_day_count[month_day_key] += 1
    
happiest_hour = max(sentiments_by_hour, key=sentiments_by_hour.get)
happiest_day = max(sentiments_by_day, key=sentiments_by_day.get)
busiest_hour = max(total_tweet_hour, key=total_tweet_hour.get)
busiest_day = max(total_tweet_day, key=total_tweet_day.get)

# the happiest hour ever, e.g. 3-4pm on 23rd November with an overall sentiment score of +12,
# the happiest day ever, e.g. 25th February was the happiest day with an overall sentiment score of +23,
# the most active hour ever, e.g. 4-5pm on 3rd March had the most tweets (#1234),
# the most active day ever, e.g. 3rd October had the most tweets (#12345),

print("Happiest hour is: " + happiest_hour + " with sentiment score: " + str(sentiments_by_hour[happiest_hour]))
print("Happiest day is: " + happiest_day + " with sentiment score: " + str(sentiments_by_day[happiest_day]))
print("Busiest hour is: " + busiest_hour + " with total number of tweets: " + str(total_tweet_hour[busiest_hour]))
print("Busiest day is: " + busiest_day + " with total number of tweets: " + str(total_tweet_day[busiest_day]))