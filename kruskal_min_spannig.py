#Kruskal min spaninng tree O(mn) version
from double_linked import *
from math import inf

class Graph(object):
	def __init__(self,fileLocation):
		file = open(fileLocation,'r')
		edges=[]
		e=file.readline()
		while e:
			ed=e.rstrip().split()
			ed=list(map(int,ed))
			edges.append(ed)
			e=file.readline()
		self.edges=edges
		file.close()
	
	def kruskal(self):
		def merg_sort(x):
			def merg(x,y):
				c=[]
				i,j=0,0
				lx,ly=len(x),len(y)
				while i<lx and j<ly:
					if x[i][-1]<=y[j][-1]:
						c.append(x[i])
						i+=1
					else:
						c.append(y[j])
						j+=1
				if i<lx:
					c+=x[i:]
				if j<ly:
					c+=y[j:]
				return c
			if len(x)==1:
				return x
			else:
				mid=len(x)//2
				return merg(merg_sort(x[:mid]),merg_sort(x[mid:]))
		
		def BFS(start,end):
			domain={}
			for i in explored:
				domain[i]=dict(explored[i])
			queue=DLL()
			domain[start]['found']=True
			queue.rappend(domain[start])
			while len(queue) != 0:
				for n in queue.head.data['neighbor']:
					if domain[n]['found'] is False:
						if n==end: 
							return True
						else:
							queue.rappend(domain[n])
							domain[n]['found']=True
				queue.lpop()
			return False
			
		Tree=[]
		explored={}
		cost=0	
		seq=merg_sort(self.edges)
		for c in seq:
			if c[0] not in explored and c[1] not in explored:# if both nodes in the same edge are not in Tree then include them
				Tree.append((c[0],c[1]))
				cost+=c[-1]
				explored[c[0]]={'index':c[0],'neighbor':[c[1]],'found':False}
				explored[c[1]]={'index':c[1],'neighbor':[c[0]],'found':False}
			else: # if one is in Tree another one is not, then do a BFS in the based on all the node that have been inluded, if can find the non-included node then do not absorb the edge to avoid loop.
				start,end=c[0],c[1]
				if c[1] in explored and c[0] not in explored:
					start,end=c[1],c[0]
				if not BFS(start,end):
					Tree.append((start,end))
					cost+=c[-1]
					if start in explored and end in explored:# if two node are in diffenrent segment, then unite these two segment by link two nodes.
						explored[start]['neighbor'].append(end)
						explored[end]['neighbor'].append(start)
					else:# the other one is totally not in the Tree
						explored[start]['neighbor'].append(end)
						explored[end]={'index':end,'neighbor':[start],'found':False}
		self.minSpanningTree=Tree
		self.cost=cost
	
		

			
			

if __name__=='__main__':	
	g=Graph('F:\py_algo\dsa\min_spanning.txt')		
	m1=g.kruskal()
	print('the minSpanningTree is:',g.minSpanningTree)
	print('the cost of the Tree is:',g.cost)


	

