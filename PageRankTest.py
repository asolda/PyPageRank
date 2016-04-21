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

#testing parallel PageRank implementation
#load balancing is done by hand

#simple is a 2 by 2 matrix
#each cell contains a subportion of the original graph 
#
#graph (partitioned matrix):
#   x y z w
#   ---
# x | |
# y | |
#   ---
# z
# w

simple = []
simple.append([])
simple[0].append(dict())
simple[0][0]['x'] = {'y'}
simple[0][0]['y'] = {'x'}
simple[0].append(dict())
simple[0][1]['x'] = {'z', 'w'}
simple[0][1]['y'] = {'w'}
simple.append([])
simple[1].append(dict())
simple[1][0]['z'] = {'x'}
simple[1][0]['w'] = {'y'}
simple[1].append(dict())
simple[1][1]['z'] = {}
simple[1][1]['w'] = {'z'}

#node degrees

degree = []
degree.append(dict())
degree[0]['x'] = 3
degree[0]['y'] = 2
degree.append(dict())
degree[1]['z'] = 1
degree[1]['w'] = 2
