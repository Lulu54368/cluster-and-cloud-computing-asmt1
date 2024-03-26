import re
import logging
sentiment_word = "sentiment"
date_word = "created_at"
sentiment_pattern = r'{}\D*(\d+\.\d*)'.format(re.escape(sentiment_word))
date_pattern = r'{}\D*(\d+)-(\d+)-(\d+)T(\d+)'.format(re.escape(date_word))  #"created_at":"2021-06-21T18:03:54.000Z",
def get_sentiment(line):
    match = re.search(sentiment_pattern, line)
    if match:
        # Get the digit right after the word
        sentiment = match.group(1)
        logging.debug("Digit right after the word '{}': {}".format(sentiment_word, sentiment))
        return float(sentiment)
    else:
        logging.warn("sentiment number not found.")
        return 0

def get_datetime(line):
    match = re.search(date_pattern, line)
    
    if match:
        logging.debug("date is ({}, {}, {})".format(match.group(2), match.group(3), match.group(4)))
        return int(match.group(2)), int(match.group(3)),int(match.group(4))
        logging.warn("Created_at not found")
    return 0,0,0