#!/usr/bin/python

import timeit
from PageRank import *

# Graph is represented with its transition matrix
simple = ([0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2], [1/3, 1/2, 0, 0])

start_time = timeit.default_timer()
time1, rank1 = pageRank(simple,0.85,75,0)
elapsed1 = timeit.default_timer() - start_time

print(rank1, time1, elapsed1)

# Graph is represented with its adjacency lists
simple = dict()
simple['x'] = {'y','z','w'}
simple['y'] = {'x','w'}
simple['z'] = {'x'}
simple['w'] = {'y','z'}

start_time = timeit.default_timer()
time2, rank2 = optPageRank(simple,0.85,75,0)
elapsed2 = timeit.default_timer() - start_time

print(rank2, time2, elapsed2)

#Suppose that we have m processors.
#We divide nodes in k=sqrt(m) subset each of size n/k, with each subset corresponding to distint subset of nodes.
#Graph is represented by a matrix of k x k blocks.
#Block[i][j] contains for every node in the i-th subset the list of its neighbors in the j-subset

#In our example, we take m = 4.
#The nodes are then divided in k=2 subsets: the 0-th subset is {'x', 'y'}, the 1-th subset is {'z', 'w'}

simple = []
simple.append([]) #The first row of blocks
simple.append([]) #The second row of blocks

#The block[0][0]
simple[0].append(dict())
simple[0][0]['x']= {'y'}
simple[0][0]['y']= {'x'}

#The block[0][1]
simple[0].append(dict())
simple[0][1]['x']= {'z','w'}
simple[0][1]['y']= {'w'}

#The block[1][0]
simple[1].append(dict())
simple[1][0]['z']= {'x'}
simple[1][0]['w']= {'y'}

#The block[1][1]
simple[1].append(dict())
simple[1][1]['z']= {}
simple[1][1]['w']= {'z'}

#Each info about the nodes of graph is represented as a vector of k blocks.
#Block[i] contains the info of nodes in the i-th subset.

#Here is the example of degree vector
degree = []

#The first block
degree.append(dict())
degree[0]['x'] = 3
degree[0]['y'] = 2

#The second block
degree.append(dict())
degree[1]['z'] = 1
degree[1]['w'] = 2

start_time = timeit.default_timer()
time3, rank3 = parallelPageRank(simple,degree,4,1,0,1,4)
elapsed3 = timeit.default_timer() - start_time

print(rank3, time3, elapsed3)