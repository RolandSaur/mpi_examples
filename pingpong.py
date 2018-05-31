"""
This is inteded to be run with 2 processes only
They will pass a number back and forth until they
end up with the number 42
"""

# import random for random stuff
from random import randint
# import mpi4py for mpi stuff
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Init the first process to a random number
if rank % 2 == 0:
    TheNumber = randint(0, 100)
else:
    TheNumber = 0


iteration = 0
while TheNumber != 42:
    if iteration % 2 == 0:  # message goes from process 0 to process 1
        if rank == 0:  # process zero sends it
            TheNumber = TheNumber + randint(-10,10)
            comm.send(TheNumber, dest=1)
        elif rank == 1:  # process one receives it
            TheNumber = comm.recv(source=0)
    else:  # message goes from process 1 to process 0
        if rank == 0:
            TheNumber = comm.recv(source=1)
        elif rank == 1:
            TheNumber = TheNumber + randint(-10, 10)
            comm.send(TheNumber, dest=0)
    iteration += 1


print("It took us %d iterations but we aggreed on %d" %
      (iteration, TheNumber))
