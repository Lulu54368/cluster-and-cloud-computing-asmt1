from utils import *
import numpy as np
import logging
import time
aggregate_data_time = 0
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def happiest_hour(sentiment_table):
    start_time = time.time()
    hour = np.unravel_index(np.argmax(sentiment_table), sentiment_table.shape)
    sentiment_number = sentiment_table[hour[0]] [hour[1]][hour[2]] 
    # remember to add one for each column 
    end_time= time.time()

    global aggregate_data_time
    aggregate_data_time = aggregate_data_time + (end_time-start_time)
    return (hour, sentiment_number) 
def most_active_hour(count_table):
    start_time= time.time()
    hour = np.unravel_index(np.argmax(count_table), count_table.shape)
    count = count_table[hour[0]] [hour[1]][hour[2]]
    end_time= time.time()
    aggregate_data_time = (end_time -start_time)
    # remember to add one for each column 
    return (hour, count) 
def happiest_day(sentiment_table):
    start_time = time.time()
    sentiment_sum_day = np.sum(sentiment_table, axis=-1)
    day = np.unravel_index(np.argmax(sentiment_sum_day), sentiment_sum_day.shape)
    sentiment_number = sentiment_sum_day[day[0]] [day[1]]
    end_time= time.time()
    aggregate_data_time = (end_time - start_time)
    return day, sentiment_number
    

def most_active_day(count_table):
    start_time = time.time()
    count_sum_day = np.sum(count_table, axis=-1)
    day = np.unravel_index(np.argmax(count_sum_day), count_sum_day.shape)
    count_number = count_sum_day[day[0]] [day[1]]
    end_time= time.time()
    aggregate_data_time = (end_time - start_time)
    return day, count_number


def print_result(count_table, sentiment_table):
    print("+++++++++++++++++Q1+++++++++++++++++")
    date, sentiment_number = happiest_hour(sentiment_table)
    month = month_dict[int(date[0])+1]
    day = int(date[1]) + 1
    hour = date[2]+1
    print(f"The happiest hour is at {hour:02d}-{hour+1:02d} {day}th of {month} with sentiment number {sentiment_number}")
    print("+++++++++++++++++Q2+++++++++++++++++")

    date, sentiment_number = happiest_day(sentiment_table)
    month = month_dict[int(date[0])+1]
    day = int(date[1]) + 1
    print(f"The happiest day is on the {day}th of {month} with sentiment number {sentiment_number}")
    print("+++++++++++++++++Q3+++++++++++++++++")
    date, count_number = most_active_hour(count_table)
    month = month_dict[int(date[0])+1]
    day = int(date[1]) + 1
    hour = date[2]+1
    print(f"The happiest hour is at {hour:02d}-{hour+1:02d} {day}th of {month} with tweets number {count_number}")
    print("+++++++++++++++++Q4+++++++++++++++++")
    date, count_number = most_active_day(count_table)
    month = month_dict[int(date[0])+1]
    day = int(date[1]) + 1
    print(f"The happiest day is on the {day}th of {month} with tweets number {count_number}")
    logging.info(f"The time taken to aggregate data for master node is {str(aggregate_data_time)} ms")
    

