import time
import logging
import numpy as np
from utils import *
start_time = time.time()
shape=(12, 31, 24)
sentiment_table = np.zeros(shape)
count_table = np.zeros(shape)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def file_reader(file_path):
    start_time = time.time()
    count = 0
    for row in open(file_path, "r"):
        count+=1
        datetime= get_datetime(row)
        sentiment =get_sentiment(row)
        sentiment_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += sentiment
        count_table[datetime[0]-1][datetime[1]-1][datetime[2]-1] += 1 
    end_time = time.time()

    logging.info("The time taken to process the file is {}ms".format(end_time-start_time))
    return 

