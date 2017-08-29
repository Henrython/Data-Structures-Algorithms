#Kruskal min_spannig tree optimized by union find

class Union(object):
	def __init__(self,length):
		self.group=[i for i in range(length+1)] 
		self.rank=[0 for i in range(length+1)]# rank is similar to depth of the tree 
		
	def find(self,i):
		'''find the leader index of vertex i and execute path contraction'''
		assert i < len(self.group)
		if self.group[i]==i:
			return i
		else:
			self.rank[i]=self.find(self.group[self.group[i]])
			return self.rank[i]
	
	def merg(self,i,j):
		'''union the two groups containing i and j'''
		li,lj=self.find(i),self.find(j)
		if li!=lj:
			ri,rj=self.rank[li],self.rank[lj]
			if ri==rj: 
				self.__leaderUpdate(li,lj)
				self.rank[lj]+=1
			elif ri<rj:
				self.__leaderUpdate(li,lj)
			else:
				self.__leaderUpdate(lj,li)
			
	def connected(self,i,j):
		'''check if i and j are connected'''
		assert i<len(self.group) and j<len(self.group)
		li,lj=self.find(i),self.find(j)
		if li==lj:
			return True
		else:
			return False
		
	def __leaderUpdate(self,v,x):
		'''update the leader of the vertex v to x(v is child, x is parent)'''
		self.group[v]=self.group[x]
	
	def __repr__(self):
		return str(self.group)


	
	