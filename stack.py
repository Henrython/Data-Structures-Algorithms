from double_linked import *
class Stack(DLL):
	def push(self,data):
		return self.rappend(data)
	def pop(self):
		return self.rpop()
	@property
	def top(self):
		return self.tail.data
	
	