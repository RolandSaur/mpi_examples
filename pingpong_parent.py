"""
This is the parent process for parent-child-pingpong example
It will
    - spawn two processes that play the ping pong game
    - receives and writes the result to the command line
"""

# import sys to get the variable passed to the python script
import sys
# import os to  get the process ID
import os
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# spawn two ping pong playing children in the sub_comm world
sub_comm = MPI.COMM_SELF.Spawn(sys.executable,
                               args=['pingpong_child.py'], maxprocs=2)

# receive the data from the the children
(iteration, TheNumber) = sub_comm.recv(source=0)

print("I am so proud of my children.")
print("It took them only %d iterations to arrive at %d" % (iteration, TheNumber))
