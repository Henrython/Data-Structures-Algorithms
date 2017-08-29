class Linked(object):
	def __init__(self,root,next=None):
		assert next is None or isinstance(next,Linked)
		self.root=root
		self.next=next
		
	def __getitem__(self,x):
		if x==0:
			return self.root
		else:
			return self.next[x-1]
	def __len__(self):
		if self.next is None:
			return 1
		else:
			return len(self.next)+1
	def __repr__(self):
		str_root=str(self.root)
		if self.next is None:
			return 'Linked({})'.format(str_root)
		else:
			return 'Linked({},{})'.format(str_root,repr(self.next))
def add(s,t):
	assert isinstance(s,Linked) and isinstance(t,Linked)
	if s.next is None:
		return Linked(s.root,t)
	else:
		return Linked(s.root,add(s.next,t))
def lmap(func,s):
	if s.next is None:
		return Linked(func(s.root))
	else:
		return Linked(func(s.root),lmap(func,s.next))
def lfilter(func,s):
	if func(s.root) is True:
		if s.next is None:
			return Linked(s.root)
		else:
			return Linked(s.root,lfilter(func,s.next))
	else:
		if s.next is None:
			return 
		else:
			return lfilter(func,s.next)
def belong(x,s):
	if x==s.root:
		return True
	else:
		if s.next is None:
			return False
		else:
			return belong(x,s.next)
def remove_duplicate(s):
	if s.next is None:
		return
	else:
		if belong(s.root,s.next):
			s.root=s.next.root
			s.next=s.next.next
			remove_duplicate(s)
		else:
			remove_duplicate(s.next)
def reverse(s):
	def drop(s):
		if s.next is not None:
			if s.next.next is None:
				s.next=None
				return
			else:
				drop(s.next)		
	if len(s)==1:
		return
	else:
		s.next,s.root=Linked(s.root,s.next),s[len(s)-1]
		drop(s.next)
		if len(s.next)>1:
			reverse(s.next)



		
s=Linked(1,Linked(2,Linked(3)))
t=Linked(4,Linked(5,Linked(6)))		
d=Linked(1,Linked(1,Linked(2,Linked(1,Linked(2)))))
#remove_duplicate(d)
reverse(s)