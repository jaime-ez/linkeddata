import operator
from igraph import *

salida=open('out-sub100.txt','r')
g=Graph.Read_GraphML('fondecyt-13429.graphml')

c=g.components()
d=map(lambda x: len(x), c)

index=sorted(enumerate(d), key=operator.itemgetter(1), reverse=True)

g2=c.subgraph(index[0][0])

g2.write_graphml("subgraf.graphml")
g2.write_dot("subgraf.dot")




#for line in salida.readlines():
#    index.append(float(line.rstrip()))
    
#index2=[]
#index2=sorted(enumerate(index), key=operator.itemgetter(1), reverse=True)

#index3=[]
#for i in range(0,99):
#	index3.append(index2[i][0])




