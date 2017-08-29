from double_linked import *
from math import inf
import re
import random
import time
file=open('F:\py_algo\min_cut.txt','r')
data=file.readlines()
l=[]
adlist={}
for i in data:
	i=i.rstrip()
	l.append(re.split('[^0-9]+',i))
for i in range(len(l)):
	adlist[i+1]=list(map(int,l[i]))
	adlist[i+1].pop(0)		

	
	
def init_data(adlist):
	dic={}
	for i in adlist:
		dic[i]={'dist':inf,'neighbor':adlist[i]}
	return dic
		
def bfs(graph,init):
	graph=init_data(graph)
	graph[init]['dist']=0
	q=DLL()
	q.rappend(init)
	while len(q)>0:
		i=q.lpop()
		for j in graph[i]['neighbor']:
			if graph[j]['dist']>=inf:
				q.rappend(j)
				graph[j]['dist']=graph[i]['dist']+1
	return graph

g={1:[3,5],3:[1,5],5:[1,3],2:[4,6,8],4:[2,6],6:[2,4,8],8:[2,6]}
print(bfs(g,4))	