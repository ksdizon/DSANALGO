# Node class

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.char = None
	
	def setChar(self, char):
		self.char = char
