from igraph import * 

g = Graph(3)
g.add_edges([(0,1),(0,2)])
print g.betweenness()       # La centralidad de todos los nodos => [1.0, 0.0, 0.0]
print g.betweenness(0)       # La centralidad solo del nodo 0 =>1
