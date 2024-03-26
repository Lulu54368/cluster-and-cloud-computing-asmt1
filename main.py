from answer_quenstion import *
from mpi4py import MPI
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start_time = time.time()
file_reader("twitter-1mb.json", rank, size)
end_time = time.time()
logging.info(f"The time taken for rank {rank} to process the file is {end_time-start_time} ms")
hour_sentiment_gathered = comm.reduce(sentiment_table, op=MPI.SUM, root=0)
hour_count_gather = comm.reduce(count_table, op=MPI.SUM, root=0)
if rank == 0:
    happiest_hour(hour_sentiment_gathered)
    most_active_hour(hour_count_gather)
    happiest_day(hour_sentiment_gathered)
    most_active_day(hour_count_gather)