# Heap class

from Node import Node

class Heap:
	head : Node
	def __init__(self, frequency_table):
		self.frequency_table = frequency_table
		
		# Creating heap
		
		while len(frequency_table) != 0:
			# Creates z node and assigns values for left and riight 
			z = Node(self.frequency_table[0][1].value + self.frequency_table[1][1].value)
			z.left = self.frequency_table[0][1]
			z.right = self.frequency_table[1][1]

			z_pair = ('z', z)
			
			# Remove nodes used to make z node
			self.frequency_table.pop(0)
			self.frequency_table.pop(0)
			
			if len(frequency_table) == 0:
				break
					
			# insert z node to table
			if z.value < self.frequency_table[0][1].value:
				self.frequency_table.insert(0, z_pair)
			else:
				self.frequency_table.insert(1, z_pair)

		self.head = z
