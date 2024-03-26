from utils import *
import numpy as np
import logging
import time

def happiest_hour(sentiment_table):
    start_time = time.time()
    hour = np.unravel_index(np.argmax(sentiment_table), sentiment_table.shape)
    sentiment_number = sentiment_table[hour[0]] [hour[1]][hour[2]] 
    # remember to add one for each column 
    end_time= time.time()
    logging.info(f"The time taken to calculate the happiest hour is {end_time-start_time} ms")
    logging.info(f"The happest hour is {hour} with number {sentiment_number}")
    return (hour, sentiment_number) 
def most_active_hour(count_table):
    start_time= time.time()
    hour = np.unravel_index(np.argmax(count_table), count_table.shape)
    count = count_table[hour[0]] [hour[1]][hour[2]]
    end_time= time.time()
    # remember to add one for each column 
    logging.info(f"The time taken to calculate the active hour is {end_time-start_time} ms")
    logging.info(f"The most active day is {hour} with number {count}")
    return (hour, count) 
def happiest_day(sentiment_table):
    start_time = time.time()
    sentiment_sum_day = np.sum(sentiment_table, axis=-1)
    day = np.unravel_index(np.argmax(sentiment_sum_day), sentiment_sum_day.shape)
    sentiment_number = sentiment_sum_day[day[0]] [day[1]]
    end_time= time.time()
    logging.info(f"The time taken to calculate the happiest hour is {end_time-start_time} ms")
    logging.info(f"The happest day is {day} with number {sentiment_number}")
    

def most_active_day(count_table):
    start_time = time.time()
    count_sum_day = np.sum(count_table, axis=-1)
    day = np.unravel_index(np.argmax(count_sum_day), count_sum_day.shape)
    count_number = count_sum_day[day[0]] [day[1]]
    end_time= time.time()
    logging.info(f"The time taken to calculate the most active day is {end_time-start_time} ms")
    logging.info(f"The most active day is {day} with number {count_number}")
