import operator
from igraph import *

salida=open('out-sub100.txt','r')
g=Graph.Read_GraphML('fondecyt-13429.graphml')
index=[]

for line in salida.readlines():
    index.append(float(line.rstrip()))
    
index2=[]
index2=sorted(enumerate(index), key=operator.itemgetter(1), reverse=True)

index3=[]
for i in range(0,99):
	index3.append(index2[i][0])

print index3
