#!/usr/bin/python

from numpy import add, dot, multiply

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
