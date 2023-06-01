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
					
			# Find the correct position to insert the z node
            		insert_index = 0
          		while insert_index < len(self.frequency_table) and self.frequency_table[insert_index][1].value < z.value:
                	insert_index += 1

            		# Insert z node into the frequency table
            		self.frequency_table.insert(insert_index, ('z', z))

		self.head = z
