#Depth first search
from stack import *

def init_data(adlist):
	dic={}
	for i in adlist:
		dic[i]={'explored':False,'neighbor':adlist[i]}
	return dic

def dfs(graph,init):
	assert init in graph
	graph=init_data(graph)
	def helper(init):
		graph[init]['explored']=True
		for n in graph[init]['neighbor']:
			if graph[n]['explored'] is False:
				helper(n)
	helper(init)
	return graph
	
g={1:[3,5],3:[1,5],5:[1,3],2:[4,6,8],4:[2,6],6:[2,4,8],8:[2,6]}
print(dfs(g,4))	
		
