module load python/3.7.4
mkdir ~/virtualenv
virtualenv  ~/virtualenv/python3.7.4/
source ~/virtualenv/python3.7.4/bin/activate
module load mpi4py/3.0.2-timed-ping-pong
module load numpy
module load logging
module load time
module load configparser
module load re
time mpiexec python3 main.py
deactivate
my-job-stats -a -h -s