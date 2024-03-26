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
        logging.debug("sentiment number not found.")
        return 0

def get_datetime(line):
    match = re.search(date_pattern, line)
    
    if match:
        logging.debug("date is ({}, {}, {})".format(match.group(2), match.group(3), match.group(4)))
        return int(match.group(2)), int(match.group(3)),int(match.group(4))
        logging.debug("Created_at not found")
    return 0,0,0



def file_reader(file_path, rank, node_number):
    count = 0
    file = open(file_path, "r")
    lines = file.readlines()
    lines_per_node = len(lines) // node_number
    remainder = len(lines) % node_number
    if(rank == 0):
        logging.debug(f"The lines for each node is {lines_per_node}")
    if (rank < remainder):
        start_index = rank * (lines_per_node+1)
        end_index = start_index + (lines_per_node + 1)
    else:
        start_index = rank * lines_per_node + remainder
        end_index = start_index + lines_per_node
    node_lines = lines[start_index:end_index]
    for row in node_lines:
        count+=1
        datetime= get_datetime(row)
        sentiment =get_sentiment(row)
        sentiment_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += sentiment
        count_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += 1 
    return 

