#!/usr/bin/python

from numpy import add, dot, multiply
from math import sqrt
from joblib import Parallel, delayed

#with prob 1 - s crawler is "teleported" (dead ends and spider traps avoidance)
#confidence: stop condition (vectors difference < confidence)
def PageRank(graph, s, step, confidence):
    done = False
    time = 0

    n = len(graph)
    #nodes' labels: 1, 2, 3, etc...
    nodes = range(n)

    rank = []
    tax = []
    for i in nodes:
        rank.append(float(1)/n)
        tax.append(float(1-s)/n)

    while not done and time < step:
        time += 1
        #original page rank would look like:
        #tmp = dot(graph, rank)
        #in this improved version with prob s I follow a link to update rank;
        #otherwise I move to a different node
        tmp = add(dot(multiply(s, graph), rank), tax)
        diff = 0
        for i in nodes:
            diff += abs(rank[i] - tmp[i])
            rank[i] = tmp[i]

        if diff <= confidence:
            done = True

    return rank, time

def OptPageRank(graph, s, step, confidence):
    nodes = graph.keys()
    n = len(nodes)

    done = False
    time = 0

    rank = dict()
    for i in nodes:
        rank[i] = float(1)/n

    tmp = dict()
    while not done and time < step:
        time += 1

        for i in nodes:
            tmp[i] = float(1-s)/n

        for i in nodes:
            for j in graph[i]:
                tmp[j] += float(s*rank[i])/len(graph[i])

        diff = 0
        for i in nodes:
            diff += abs(rank[i] - tmp[i])
            rank[i] = tmp[i]

        if diff <= confidence:
            done = True

    return rank, time

# multiply a block of the matrix and a block of the vector
def execute(sgraph, sdegree, srank, s):
    nodes = sgraph.keys()
    
    tmp = dict()
    
    for i in nodes:
        for j in sgraph[i]:
            if j not in tmp:
                tmp[j] = 0
            tmp[j] = float(s*rank[i])/sdegree[i]
            
    return tmp


# param n is number of nodes
def ParallelPageRank(graph, degree, n, s, step, confidence, num_jobs):
    done = False
    time = 0
    
    k = int(sqrt(num_jobs))

    # init

    rank = []
    
    for i in range(k):
        rank[i] = dict()
        for j in degree[i].keys():
            rank[i][j] = float(1)/n
            
    tmp = []
    for i in range(k):
        tmp[i] = dict()

    # add backend = "threading" to spawn thread insted of processes
    with Parallel(n_jobs=num_jobs) as parallel:
        while not done and time < step:
            time += 1
            
            result=parallel(delayed(execute)(graph[i][j], degree[i], rank[i], s)
                for j in range(k) for i in range(k))
            
            return result
    return time, rank