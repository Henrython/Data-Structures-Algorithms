class Node(object):
	def __init__(self,data,next=None,prev=None):
		assert data is not None
		self.data=data
		self.prev=prev
		self.next=next
	def __repr__(self):
		prev_str='<--'
		next_str='-->'
		data_str=repr(self.data)
		return prev_str+data_str+next_str
class DLL(object):
	def __init__(self,head=None):
		if head:
			head=Node(head)
		self.head=head
		self.tail=self.head
	def rappend(self,n):
		n=Node(n)
		if self.tail:
			self.tail.next=n
			n.prev=self.tail
			self.tail=n
		else:
			self.head=n
			self.tail=self.head
	def lappend(self,n):
		if self.head:
			n=Node(n)
			self.head.prev=n
			n.next=self.head
			self.head=n
		else:
			self.rappend(n)
	def __len__(self):
		l=0
		trace=self.head
		while trace:
			l+=1
			trace=trace.next
		return l
	def __getitem__(self,i):
		assert 0<=i<len(self),'IndexError'
		if i<len(self)//2:
			trace=self.head
			while i>0:
				trace=trace.next
				i-=1
			return trace
		else:
			trace=self.tail
			while i<len(self)-1:
				trace=trace.prev
				i+=1
			return trace
	def rpop(self):
		if not self.tail:
			raise IndexError('pop from a empty list')
		cache=self.tail.data
		if self.head==self.tail:
			self.head=None
			self.tail=None
		else:
			self.tail.prev.next=None
			self.tail=self.tail.prev
		return cache
	def lpop(self):
		if not self.head:
			raise IndexError('pop from a empty list')
		cache=self.head.data
		if self.head==self.tail:
			self.head=None
			self.tail=None
		else:
			self.head.next.prev=None
			self.head=self.head.next
		return cache
	def remove(self,i):
		if self.head==self.tail:
			raise IndexError('remove from a empty list')
		if not 0<=i<=len(self)-1:
			raise IndexError('Index out of range')
		if i==0:self.lpop()
		elif i==len(q)-1:self.rpop()
		else:
			if i<len(self)//2:
				trace=self.head
				while i>0:
					trace=trace.next
					i-=1
			else:
				trace=self.tail
				while i<len(self)-1:
					trace=trace.prev
					i+=1
			trace.prev.next=trace.next
			trace.next.prev=trace.prev
					
	def insert(self,n,i):
		if not 0<=i<=len(self)-1:
			raise IndexError('Index out of range')
		if i==0:self.lappend(n)
		elif i==len(self)-1:self.rappend(n)
		else:
			n=Node(n)
			if i<len(self)//2:
				trace=self.head
				while i>0:
					trace=trace.next
					i-=1
			else:
				trace=self.tail
				while i<len(self)-1:
					trace=trace.prev
					i+=1
			trace.prev.next=n
			n.prev=trace.prev
			n.next=trace
			trace.prev=n	
	def __repr__(self):
		sequence_str=''
		trace=self.head
		while trace:
			sequence_str+=repr(trace)
			trace=trace.next
		return sequence_str
	def __add__(self,l):
		assert isinstance(l,DLL)
		c=DLL()
		trace1=self.head
		while trace1:
			c.rappend(trace1.data)
			trace1=trace1.next
		trace2=l.head
		while trace2:
			c.rappend(trace2.data)
			trace2=trace2.next
		return c
	def __radd__(self,l):
		return l.__add__(self)
	def reverse(self):
		trace=self.head
		while trace:
			trace.prev,trace.next=trace.next,trace.prev
			trace=trace.prev
		self.head,self.tail=self.tail,self.head
	
			
	
		

		
	
	
	
	
	
	
	