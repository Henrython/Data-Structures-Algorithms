def init_data(adlist):
	dic={}
	for i in adlist:
		dic[i]={'explored':False,'label':None,'neighbor':set(adlist[i])}
	return dic

def dfs(graph,init):
	global current_label
	assert init in graph
	graph[init]['explored']=True
	for n in graph[init]['neighbor']:
		if graph[n]['explored'] is False:
			dfs(graph,n)
	graph[init]['label']=current_label
	current_label-=1

	
def topo_sort(graph):
	#global current_label
	graph=init_data(graph)
	for i in graph:
		if graph[i]['explored'] is False:
			dfs(graph,i)
	return graph


def topo_sort_recur(graph,init_label,cache=set()):
	for i in graph:
		if graph[i]['explored'] is False and len(graph[i]['neighbor']-cache)==0:
			cache.add(i)
			graph[i]['label']=init_label
			graph[i]['explored']=True
			init_label-=1
			topo_sort_recur(graph,init_label,cache)
	return graph
			
		
			
			
	
	

g=init_data({4:[],3:[2,6,7],1:[2,3],2:[5,4],5:[4],6:[5],7:[6]})
current_label=len(g) 
print(topo_sort_recur(g,current_label))	