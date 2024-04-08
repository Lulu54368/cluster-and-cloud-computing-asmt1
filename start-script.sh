#!/bin/sh
#SBATCH --partition=cascade
#SBATCH --nodes=8
#SBATCH --time=00:30:00
module --ignore_cache load "Python/3.10.4"
mkdir ~/virtualenv
virtualenv  ~/virtualenv/python3.10.4/
source ~/virtualenv/python3.10.4/bin/activate
pip3 install mpi4py
pip3 install numpy
pip3 install datetime
pip3 install regex
time mpiexec python3 main.py
deactivate
my-job-stats -a -h -s