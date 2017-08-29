#min spanning tree
class Heap(object):
	def __init__(self,data=[]):
		assert isinstance(data,list)
		self.size=len(data)
		self.data=data
		self.pos=[0]+[i for i in range(0,self.size)]
		for j in range(self.size-1,-1,-1):
			self.sink(j)
	
	def parent(self,i):
		assert 0<=i<self.size
		if i!=0: return (i-1)//2
	
	def left(self,i):
		if (i*2+1)>=self.size:
			return None
		else:
			return i*2+1
	
	def right(self,i):
		if (i+1)*2>=self.size:
			return None
		else:
			return (i+1)*2
	
	def is_heap(self,i):
		if self.left(i):
			l=self.left(i)
			if self.data[i]['dist']>self.data[l]['dist']:return False
			else:
				if self.right(i):
					r=self.right(i)
					if self.data[i]['dist']>self.data[r]['dist']:return False
					else: return True
				else:return True
		else: return True
					
	def exch(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
		self.pos[self.data[i]['index']],self.pos[self.data[j]['index']]=self.pos[self.data[j]['index']],self.pos[self.data[i]['index']]
	
	def sink(self,i):
		curr_pos=i
		l=self.left(curr_pos)
		r=self.right(curr_pos)
		while not self.is_heap(curr_pos):
			if l and not r:
				self.exch(curr_pos,l)
				curr_pos=l
				l=self.left(curr_pos)
				r=self.right(curr_pos)
			else:
				if self.data[l]['dist']<self.data[r]['dist']:
					self.exch(curr_pos,l)
					curr_pos=l
					l=self.left(curr_pos)
					r=self.right(curr_pos)
				else:
					self.exch(curr_pos,r)
					curr_pos=r
					l=self.left(curr_pos)
					r=self.right(curr_pos)
	
	def bubble(self,i):
		curr_pos=i
		while curr_pos!=0:
			if self.data[curr_pos]['dist']>=self.data[self.parent(curr_pos)]['dist']:
				break
			self.exch(curr_pos,self.parent(curr_pos))
			curr_pos=self.parent(curr_pos)
		
	def _insert(self,data):
		self.data.append(data)
		curr_pos=self.size-1
		self.bubble(curr_pos)
		self.size+=1
		
	def extract_min(self):
		self.size-=1
		min=self.data[0]
		self.exch(0,-1)
		self.pos[self.data[-1]['index']]=inf
		self.data.pop()
		self.sink(0)
		return min
	def de_key(self,i,d):
		'''decrease the key value to d, and bubble the vertex up'''
		pos=self.pos[i]
		self.data[pos]['dist']=d
		self.bubble(pos)
	def get_key(self,i):
		'''get the key value of the i th vertex'''
		return self.data[self.pos[i]]['dist']
	def is_inheap(self,i):
		'''check if vertex i in the heap'''
		if self.pos[i]<inf:return True
		else:return False
	def set_head(self,vertex,head):
		self.data[self.pos[vertex]]['head']=head


from math import inf
class Graph(object):

	def __init__(self,fileLocation):
		file=open(fileLocation,'r')
		l=[]
		i=file.readline()
		while i:
			i=i.split()
			i[0]=int(i[0])
			for j in range(1,len(i)):
				i[j]=list(map(int,i[j].split(',')))
			l.append({'index':i[0],'neighbor':[n for n in i[1:]],'dist':inf,'head':None})
			i=file.readline()
		self.map=l
		file.close()
		
	def heapify(self):
		l=[]
		for i in self.map:
			l.append(dict(i))
		self.heap=Heap(l)
	
	def min_spanningTree(self,start):
		self.map[start-1]['dist']=0
		self.map[start-1]['explored']=True
		self.heapify()
		Tree=[]
		cos=0
		while self.heap.size>0:
			v=self.heap.extract_min()
			for n in v['neighbor']:
				cost=n[-1]
				if self.heap.is_inheap(n[0]) and cost<self.heap.get_key(n[0]):
					self.heap.de_key(n[0],cost)
					self.heap.set_head(n[0],v['index'])
			Tree.append((v['head'],v['index']))
			cos+=v['dist']
		self.Tree=Tree
		self.cost=cos
		

if __name__=='__main__':		
	gg=Graph('F:\py_algo\dsa\min_spanning_list.txt')
	gg.min_spanningTree(1)
	print('the minSpanningTree is:',gg.Tree)
	print('the cost of the Tree is:',gg.cost)	
		
	
		