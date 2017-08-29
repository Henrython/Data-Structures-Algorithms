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

def replace(x,y,z):
	if x==y:return z
	else:return x
def min_cut(graph):
	if len(graph)==2:
		return len(graph[int(list(graph.keys())[0])])
	else:
		i=random.sample(list(graph.keys()),1)[0]
		j=random.sample(graph[i],1)[0]
		for e in graph[j]:
			if e!=i:
				graph[e]=[replace(x,j,i) for x in graph[e]]
		graph[i]=graph[i]+graph[j]
		graph[i]=[e for e in graph[i] if e!=i and e!=j]
		graph.pop(j)
		return min_cut(graph)
#{1:[2,5],2:[3,4,1,5],3:[2,4,5],4:[2,3,5],5:[2,1,3,4]}
def min_cut_routine(graph):
	from math import log
	out=[]
	n=len(graph)
	iter=n
	for i in range(iter):
		gg=dict(graph)
		out.append(min_cut(gg))
	return min(out)
def time_test():
	time0=time.clock()
	min_cut(adlist)
	print(time.clock()-time0)
	

print(min_cut_routine(adlist))	