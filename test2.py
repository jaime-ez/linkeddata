import operator
from igraph import *

salida=open('out.txt','a')
g=Graph.Read_GraphML('fondecyt-13429.graphml')
top=[]
for i in range(len(g.vs)):
    g.vs[i]['betweeness']=g.betweenness(i,directed=True,cutoff=5)
    top.append(g.vs[i]['betweeness'])
    print top[i]
    salida.write(str(top[i])+'\n')


index=sorted(enumerate(top), key=operator.itemgetter(1), reverse=True)
index2=[]
for i in range(0, 99):
    index2.append(index[i][0])

g2=g.subgraph(index2)
g2.write_graphml("subgrafo-100-betwen.graphml")

g2.write_dot("subgrafo-100-betwen.dot")

subprocess.call(["neato", "subgrafo-100-betwen.dot",
                 "-Tpdf",
                 "-o" + "subgrafo-100-betwen.pdf"])
