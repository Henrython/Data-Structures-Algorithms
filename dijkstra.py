# dijkstra short path and min spanning tree
import re
from math import inf
#Binary heap(min-heap)
class Heap(object):
	def __init__(self,data=[]):
		assert isinstance(data,list)
		i=len(data)
		self.data=data
		self.pos=[0]+[i for i in range(0,i)]
		for j in range(i-1,-1,-1):
			self.sink(j)
	@property
	def size(self):
		return len(self.data)
	
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
		
	def extract_min(self):
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
	
	
			
		
class Graph(object):
	def __init__(self,fileLocation):
		file = open(fileLocation,'r')
		l=[]
		ad=[]
		da=file.readlines()
		for i in da:
			i=i.rstrip()
			l.append(re.split('\t',i))
		for i in l:
			ad.append({'index':int(i[0]),'dist':inf,'explored':None,'neighbor':[list(re.split(',',j)) for j in i[1:]]})
			for k in range(len(ad[-1]['neighbor'])):
				ad[-1]['neighbor'][k]=list(map(int,ad[-1]['neighbor'][k]))
		
		self.map=ad
		self.heap_data=list(ad)
		file.close()
	def heapify(self):
		self.heap=Heap(self.heap_data)
	def set_d(self,i,d):
		'''update the optimal distance for vertex i'''
		self.map[i-1]['dist']=d
		self.map[i-1]['explored']=True

	def dijkstra(self,start,end=None):
		self.heapify()
		self.heap.de_key(start,0)
		while self.heap.size>0:
			v=self.heap.extract_min()
			pos=v['index']
			dist=v['dist']
			self.set_d(pos,dist)
			if pos==end:break
			else:
				for u in self.map[pos-1]['neighbor']:
					new_dist=dist+u[1]
					if self.heap.is_inheap(u[0]) and new_dist<self.heap.get_key(u[0]):
						self.heap.de_key(u[0],new_dist)
		return self.map
	
	

		
		
		
		
		