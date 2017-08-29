# min_spanning tree optimized by union find
from UnionFind import Union
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
		self.edges=edges# all the edges:the head,tail,cost for every edges 
		file.close()
		v=0
		for i in self.edges:
			mx=max(i[0],i[1])
			if mx>v:
				v=mx
		self.union=Union(v)# initialize the union
	
	def Kruskal(self):
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

		Tree=[]
		cost=0	
		seq=merg_sort(self.edges)				
		
		for e in seq:
			if not self.union.connected(e[0],e[1]):# if new node not in the Tree then include it
				Tree.append((e[0],e[1]))
				self.union.merg(e[0],e[1])# absorb the new node into unnion
				cost+=e[-1]# update the edge cost
		self.minSpanningTree=Tree
		self.cost=cost
		print(Tree)
		print(cost)

if __name__=='__main__':
	g=Graph('F:\py_algo\dsa\min_spanning.txt')
	g.Kruskal()
			