#!/usr/bin/python

from PageRank import OptPageRank

def readGraph(filename) :
    infile = open(nomefile, "r")
    graph = dict()
    for line in infile:
        if "#" not in line:
            u, v = line.split()
            if u not in graph:
                graph[u] = set()
            # directed graphs
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)
    return graph

graph = readGraph("cit-dataset")