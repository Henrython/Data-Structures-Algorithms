from double_linked import DLL
class Node(object):
	def __init__(self,key,value=[],color='red',left=None,right=None):
		self.key=key
		self.val=value
		self.left=left
		self.right=right
		self.color=color
		
class BST(object):
	def __init__(self):
		self.root=None
		self.size=0
	
	def key_size(self):
		def helper(root=self.root):
			if root==None:
				return 0
			else:
				return helper(root.left)+helper(root.right)+1
		return helper()
	
	def search(self,key):
		'''find the node with the given key'''
		root=self.root
		while root:
			if key>root.key:
				root=root.right
			elif key<root.key:
				root=root.left
			else:
				return root
		return False
	
	def insert(self,key,value):
		'''insert a node into binary search tree'''
		def push(root,key,value):
			if root==None:
				return Node(key,value)
			if root.key<key:
				root.right=push(root.right,key,value)
			elif root.key>key:
				root.left=push(root.left,key,value)
			elif roo.key==key:
				root.val+=value
			if self.__isRed(root.right) and not self.__isRed(root.left):
				root=self.rotate_left(root)
			if self.__isRed(root.left) and self.__isRed(root.left.left):
				root=self.rotate_right(root)
			if self.__isRed(root.left) and self.__isRed(root.right):
				self.flip_color(root)
			return root
		self.root=push(self.root,key,value)
		self.size+=1
	
	def floor(self,key):
		'''find a node with the largest key that is smaller than the given key'''
		def helper(key,root=self.root):
			if root==None: return None
			if root.key==key: return root
			elif root.key>key:
				return helper(key,root.left)
			elif root.key<key:
				t=helper(key,root.right)
				if t is not None:
					return t
				else:
					return root
		return helper(key)

	def ceil(self,key):
		'''find a node with smallest key that is larger than the given key'''
		def helper(key,root=self.root):
			if root==None: return None
			if root.key==key: return root
			elif root.key<key:
				return helper(key,root.right)
			elif root.key>key:
				t=helper(key,root.left)
				if t is not None:
					return t
				else:
					return root
		return helper(key)		
	
	def in_order(self):
		''' traverse the tree in ascending order'''
		queue=DLL()
		
		def helper(root):
			if root is None:return
			helper(root.left)
			queue.rappend(root.key)
			helper(root.right)
		helper(self.root)
		return queue
	
	def __isRed(self,node):
		if node is None: return False
		else: return node.color=='red'
	
	def rotate_left(self,node):
		if self.__isRed(node.right):
			root = node.right
			node.color='red'
			root.color='black'
			node.right=root.left
			root.left=node
			return root
	
	def rotate_right(self,node):
		if self.__isRed(node.left) and self.__isRed(node.left.left):
			root=node.left
			node.left=root.right
			root.right=node
			node.color='red'
			root.color='black'
			return root
	
	def flip_color(self,node):
		if self.__isRed(node.left) and self.__isRed(node.right):
			node.left.color='black'
			node.right.color='black'
			node.color='red'
		
	
	
if __name__=='__main__':	
	T=BST()
	for i in range(1,10000):
		T.insert(i,i+1)