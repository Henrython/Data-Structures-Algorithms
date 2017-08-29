#Binary heap(min-heap)
class Heap(object):
	def __init__(self,data=[]):
		assert isinstance(data,list)
		self.size=len(data)
		self.data=data
		for j in range(self.size-1,-1,-1):
			self.sink(j)
	
	#@property
	#def size(self):
	#	return len(self.data)
	
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
			if self.data[i].key>self.data[l].key:return False
			else:
				if self.right(i):
					r=self.right(i)
					if self.data[i].key>self.data[r].key:return False
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
				if self.data[l].key<self.data[r].key:
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
			if self.data[curr_pos].key>=self.data[self.parent(curr_pos)].key:
				break
			self.exch(curr_pos,self.parent(curr_pos))
			curr_pos=self.parent(curr_pos)
		
	def insert(self,data):
		self.data.append(data)
		self.size+=1
		curr_pos=self.size-1
		self.bubble(curr_pos)
		
		
	def extract_min(self):
		min=self.data[0]
		self.exch(0,-1)
		self.data.pop()
		self.size-=1
		self.sink(0)
		
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
					
	# def _extract_procedure(self,j):
		# '''like the extract_min method, but exchange the top with the j th postion then pop out the j th vertex and sink the top vertex'''
		# self._exch_procedure(0,j)
		# self._sink_procedure(0)
	
	def heapsort(self):
		j=self.size-1
		while j>0:
			self._exch_procedure(0,j)
			self._sink_procedure(0,j)
			j-=1
		return self.data

class Node(object):
	def __init__(self,key,letter=None,right=None,left=None):
		self.key=key
		self.letter=letter
		self.right=right
		self.left=left
		
	def __repr__(self):
		return str(self.key)	
		
class Huffman_Tree(object):
	def __init__(self,fileLocation):
		file = open(fileLocation,'r')
		dic={}
		i=file.read(1)
		while i:
			if i.isalpha():
				if i in dic:dic[i]['key']+=1
				else: dic[i]={'key':1,'letter':i,'code':None}
			i=file.read(1)
		file.close()
		self.dic=dic
	
	def _heapify(self):
		self.heap=Heap()
		for i in self.dic:
			self.heap.insert(Node(self.dic[i]['key'],i))
	
	def _build_tree(self):
		while self.heap.size>2:
			a=self.heap.extract_min()
			b=self.heap.extract_min()
			c=Node(a.key+b.key)
			c.left=a
			c.right=b
			self.heap.insert(c)
		self.root=Node(None)
		a=self.heap.extract_min()
		b=self.heap.extract_min()
		self.root.left=a
		self.root.right=b
	
	def _encoding(self):
		def healper(start=self.root,code=''):
			if start.letter:
				self.dic[start.letter]['code']=code
			if start.left:
				healper(start.left,code+'0')
			if start.right:
				healper(start.right,code+'1')
		healper()
	
	def print_tree(self):
		for i in self.dic:
			print(i,':',self.dic[i]['code'])
		
		
		
h=Huffman_Tree('F:\py_algo\dsa\huffman.txt')	
h._heapify()
h._build_tree()
h._encoding()			
			