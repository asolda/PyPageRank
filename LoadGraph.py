#!/usr/bin/python

import timeit
from PageRank import optPageRank

# Consider the High-energy physics citation network
# available at https://snap.stanford.edu/data/cit-HepPh.txt.gz
# and compute the Page Rank of nodes in this network with confidence
# 0 and s = 0.9.
#
# Find the best tradoff between confidence level and computation time
#
# Find how the parameter s influences this tradoff

def readGraph(nomefile):
  infile = open(nomefile,"r")
  graph = dict()
  for line in infile:
    if "#" not in line:
      u,v = line.split()
      if u not in graph:
        graph[u] = set()
      graph[u].add(v)
  return graph

graph=readGraph("cit-HepPh.txt")

start_time = timeit.default_timer()
time, rank = optPageRank(graph,0.9,150,10**(-8))
elapsed = timeit.default_timer() - start_time

print("s=0.9","; confidence =", 10**(-8), "; step =", time)
print("time:", elapsed)

for j in range(6):
  start_time = timeit.default_timer()
  time, tmp = optPageRank(graph,0.9,150,10**(-j-1))
  elapsed = timeit.default_timer() - start_time
  
  diff = 0
  for i in graph.keys():
    diff += abs(rank[i]-tmp[i])
    
  print("s=0.9","; confidence =", 10**(-j-1), "; step =", time)
  print("time:", elapsed, "; distance:", diff)
  
j = 50
while j < 150:
  start_time = timeit.default_timer()
  time, tmp = optPageRank(graph,0.9,j,10**(-8))
  elapsed = timeit.default_timer() - start_time
  
  diff = 0
  for i in graph.keys():
    diff += abs(rank[i]-tmp[i])
    
  print("s=0.9","; confidence =", 10**(-8), "; step =", time)
  print("time:", elapsed, "; distance:", diff)
  
  j += 5
  
k = 1
while k > 0.5:
  start_time = timeit.default_timer()
  time, tmp = optPageRank(graph,k,150,10**(-8))
  elapsed = timeit.default_timer() - start_time
  
  diff = 0
  for i in graph.keys():
    diff += abs(rank[i]-tmp[i])
    
  print("s=",k,"; confidence =", 10**(-8), "; step =", time)
  print("time:", elapsed, "; distance:", diff)
  
  k -= 0.05