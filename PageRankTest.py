#!/usr/bin/python

import timeit

from PageRank import *

simple = ([0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2], [1/3, 1/2, 0, 0])

start = timeit.default_timer()
rank, time = PageRank(simple, 0.85, 75, 0)
elapsed = timeit.default_timer() - start

print(rank, time, elapsed)

#testing with different representation and optimized PageRank

simple = dict()
simple[0] = {1, 2, 3}
simple[1] = {0, 3}
simple[2] = {0}
simple[3] = {1, 2}

start = timeit.default_timer()
rank, time = OptPageRank(simple, 0.85, 75, 0)
elapsed = timeit.default_timer() - start
print(rank, time, elapsed)
