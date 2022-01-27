from os import stat
import queue
import copy
from turtle import st

"""Breath First algorithm."""
# Create a Queue
# Create a set to add visited states.
# Add stating state to queue
# Take the first item in queue and add it to visited list
# Create a list of the possible states from the current state. Add those which are not within the visited list to the rear of the queue.
# Repeat untill queue is empty
