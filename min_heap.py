#Binary heap(min-heap)
class Heap(object):
	def __init__(self,data=[]):
		assert isinstance(data,list)
		self.size=len(data)
		self.data=data
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
			if self.data[i]>self.data[l]:return False
			else:
				if self.right(i):
					r=self.right(i)
					if self.data[i]>self.data[r]:return False
					else: return True
				else:return True
		else: return True
					
	def exch(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
	
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
				if self.data[l]<self.data[r]:
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
			if self.data[curr_pos]>=self.data[self.parent(curr_pos)]:
				break
			self.exch(curr_pos,self.parent(curr_pos))
			curr_pos=self.parent(curr_pos)
		
	def insert(self,data):
		self.data.append(data)
		curr_pos=self.size-1
		self.bubble(curr_pos)
		self.size+=1
		
	def extract_min(self):
		min=self.data[0]
		self.exch(0,-1)
		self.data.pop()
		self.sink(0)
		self.size-=1
		return min
		
	def _exch_procedure(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
			
	def _sink_procedure(self,i,j):
		'''like the sink method, but stop when the vertex hit the j th position'''
		curr_pos=i
		l=self.left(curr_pos)
		r=self.right(curr_pos)
		while not self.is_heap(curr_pos):
			if not curr_pos<self.parent(j):break
			if l and not r:
				self.exch(curr_pos,l)
				curr_pos=l
				l=self.left(curr_pos)
				r=self.right(curr_pos)
			else:
				if self.data[l]<self.data[r]:
					self.exch(curr_pos,l)
					curr_pos=l
					l=self.left(curr_pos)
					r=self.right(curr_pos)
				else:
					self.exch(curr_pos,r)
					curr_pos=r
					l=self.left(curr_pos)
					r=self.right(curr_pos)
					
	def heapsort(self):
		j=self.size-1
		while j>0:
			self._exch_procedure(0,j)
			self._sink_procedure(0,j)
			j-=1
		return self.data

if __name__=='__main__':		
	from random import randint		
	h=Heap([randint(1,100000) for i in range(100000)])
	print(h.heapsort())

		
			
			