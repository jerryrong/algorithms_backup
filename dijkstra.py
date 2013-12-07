# coding: utf-8
"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.
 
Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.
 
You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. Please type your answer in the space provided.
 
IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""
 
G = {}
 
with open('dijkstraData.txt', 'r') as src:
    for line in src:
        words = line.rstrip().split('\t')
        vertex = int(words[0])
        G[vertex] = [tuple(map(int, word.split(','))) for word in words[1:]]
 
# vertices processed so far
X = set()
 
# computed short-path distances
A = dict()
 
# all vertices of a graph
V = set(G.keys())
 
X.add(1)
A[1] = 0
 
while X != V:
    Xminpath = 1000000
    Xminvertex = None
 
    for v in X:
        minvertex = None
        minpath = 1000000
 
        for w, weight in G[v]:
            if w not in X and A[v] + weight < minpath:
                minpath = A[v] + weight
                minvertex = w
 
        if minpath < Xminpath:
            Xminpath = minpath
            Xminvertex = minvertex
 
    A[Xminvertex] = Xminpath
    X.add(Xminvertex)
 
# shortest distances to the given vertices
print A[7], A[37], A[59], A[82], A[99], A[115], A[133], A[165], A[188], A[197]
