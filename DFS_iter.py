from stack import *
def init_data(adlist):
	dic={}
	for i in adlist:
		dic[i]={'explored':False,'leader':None,'neighbor':set(adlist[i])}
	return dic

def dfs(graph,init_point):
	global current_label
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
				graph[s.top]['label']=current_label
				current_label-=1
				s.pop()
time=0
finish_time={}
def path1(graph,init_point):
	global time
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

g={1:[7],2:[5],3:[9],4:[1],5:[8],6:[3,8],7:[4,9],8:[2],9:[6]}
graph=init_data(g)
for i in graph:
	path1(graph,i)
	