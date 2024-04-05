import re
import logging
import time
import numpy as np

start_time = time.time()
shape=(12, 31, 24)
sentiment_table = np.zeros(shape)
count_table = np.zeros(shape)

sentiment_word = "sentiment"
date_word = "created_at"
sentiment_pattern = r'\"{}\"\D*:(-*\d+(\.\d*)*)'.format(re.escape(sentiment_word))
date_pattern = r'{}\D*(\d+)-(\d+)-(\d+)T(\d+)'.format(re.escape(date_word))  #"created_at":"2021-06-21T18:03:54.000Z",
def get_sentiment(line):
    match = re.search(sentiment_pattern, line)
    if match:
        # Get the digit right after the word
        sentiment = match.group(1)
        logging.debug("Digit right after the word '{}': {}".format(sentiment_word, sentiment))
        return float(sentiment)
    else:
        logging.debug("sentiment number not found.")
        return 0

def get_datetime(line):
    match = re.search(date_pattern, line)
    
    if match:
        logging.debug("date is ({}, {}, {})".format(match.group(2), match.group(3), match.group(4)))
        return int(match.group(2)), int(match.group(3)),int(match.group(4))
    else:
        logging.debug("Created_at not found")
    return 0,0,0



def file_reader(file_path, rank, node_number):
    count = 0
    file = open(file_path, "r")
    lines = []
    line = file.readline()
    count = 0
    try:
        while line:
            lines.append(line.strip()) 
            line = file.readline()
            if count % node_number == rank: 
                logging.debug(f"count {count} assigned to {rank}")
                datetime= get_datetime(line)
                sentiment =get_sentiment(line)
                sentiment_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += sentiment
                count_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += 1 
            count += 1
        logging.info(f"finished reading with tot line number {count}")
    except:
        logging.error(f"Error occurred in line {count}")
    
    return 

