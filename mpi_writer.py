"""
process with rank 0 receives data and writes it to a csv file
the name of the csv file should be passed to the process
"""

# import sys to get the variable passed to the python script
import sys
# import os to  get the process ID
import os
from mpi4py import MPI


filename = sys.argv[1]
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# augment filename so that every process writes to their own specific file
filename = filename
# print("hello from process number", rank)

# get the process ID
data = os.getpid()

# collect data from the other processes
newdata = comm.gather(data, root=0)

if rank == 0:
    with open(filename, "w") as test_file:
        for i in newdata: # loop over all the data that  was collected
            test_file.write("I am %d and need to do this for %d \n" % (os.getpid(), i))
            if i == os.getpid():
                test_file.write("Ohh wait that's me \n")
