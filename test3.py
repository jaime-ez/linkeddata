import operator
from igraph import *

salida=open('out-sub100.txt','a')
g=Graph.Read_GraphML('fondecyt-13429.graphml')
index=[]

for line in salida.readlines():
    index.append(int(line))
    
index2=[]
index2=sorted(enumerate(index), key=operator.itemgetter(1), reverse=True)

print index2
