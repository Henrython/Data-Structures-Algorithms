#strongly connected component
import re
import time
from stack import *
file =open('F:\py_algo\dsa\scc.txt','r')
data=file.readlines()
l=[]
graph={}
rgraph={}
for i in data:
	i=i.rstrip()
	l.append(list(map(int,re.split('[^0-9]+',i))))
for i in l:
	if i[0] in graph:
		graph[i[0]]['neighbor'].add(i[1])
	else:
		graph[i[0]]={'neighbor':{i[1]},'explored':False,'leader':None}
for i in range(1,max(graph)+1):
	if i not in graph:
		graph[i]={'neighbor':set(),'explored':False,'leader':None}	
for i in l:
	if i[1] in rgraph:
		rgraph[i[1]]['neighbor'].add(i[0])
	else:
		rgraph[i[1]]={'neighbor':{i[0]},'explored':False,'leader':None}
for i in range(1,max(graph)+1):
	if i not in rgraph:
		rgraph[i]={'neighbor':set(),'explored':False,'leader':None}

def Kosaraju(graph,rgraph):
	time=0
	lead=None
	finish_time={}
	scc={}
	
	def path1(graph,init_point):
		nonlocal time
		if graph[init_point]['explored'] is False:
			graph[init_point]['explored']=True
			s=Stack(init_point)
			while len(s)>0:
				check=True
				for i in graph[s.top]['neighbor']:
					if graph[i]['explored'] is False:
						check=False
						graph[i]['explored']=True
						s.push(i)
						break
				if check:
					time+=1
					finish_time[time]=s.top
					s.pop()
		
	def path2(graph,init_point):
		nonlocal lead
		graph[init_point]['explored']=True
		graph[init_point]['leader']=lead
		scc[lead]=1
		s=Stack(init_point)
		while len(s)>0:
			check=True
			for i in graph[s.top]['neighbor']:
				if graph[i]['explored'] is False:
					check=False
					graph[i]['explored']=True
					graph[i]['leader']=lead
					scc[lead]+=1
					s.push(i)
					break
			if check:
				s.pop()
	
	for i in rgraph:
		path1(rgraph,i)
	for i in range(max(finish_time),min(finish_time)-1,-1):
		if graph[finish_time[i]]['explored'] is False:
			lead=i
			path2(graph,finish_time[i])			
	return scc

	
scc_g=Kosaraju(graph,rgraph)

# def init_data(adlist):
	# dic={}
	# for i in adlist:
		# dic[i]={'explored':False,'leader':None,'neighbor':set(adlist[i])}
	# return dic
# def reverse(graph):
	# rgraph={}
	# for i in graph:
		# rgraph[i]={'explored':False,'neighbor':set(),'leader':None}
		# for j in graph:
			# if j!=i:
				# if i in graph[j]['neighbor']:
					# rgraph[i]['neighbor'].add(j)
	# return rgraph
# g={1:[7,1],2:[5],3:[9],4:[1],5:[8],6:[3,8],7:[4,9],8:[2],9:[6]}
# rgraph=init_data(g)
# graph={1:[4,1],4:[7],7:[1],9:[7,3],3:[6],6:[9],8:[6,5],5:[2],2:[8]}
# graph=init_data(graph)
# print(Kosaraju(graph,rgraph))
