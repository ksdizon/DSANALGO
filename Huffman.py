# Huffman Algorithm

from Node import Node
from Heap import Heap

def createTable(text):
	frequency_table = {}
	# create frequency table
	for char in text:
		if char not in frequency_table:
			new_node = Node(1)
			new_node.setChar(char)
			frequency_table[char] = new_node
		else:
			frequency_table[char].value += 1
	
	# Sort frequency table. Changes dict to list containg sets
	frequency_table = sorted(frequency_table.items(), key = lambda item:item[1].value)
	
	return frequency_table

def createHeap(frequency_table):
	thisHeap = Heap(frequency_table)
	
	return thisHeap

def huffman(head, huffman_table, current_code = ''):
	if head.char == None:
		huffman(head.left, huffman_table, current_code + "0")
		huffman(head.right, huffman_table, current_code + "1")
	else:
		huffman_table[head.char] = current_code
		
	return huffman_table

def main():
	text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccccccccddddddddddddddddeeeeeeeeefffff'
	frequency_table = createTable(text)

	myHeap = createHeap(frequency_table)
	print(myHeap.head.right.right.value)
	
	# initialize huffman dict
	huffman_table = {}
	x = huffman(myHeap.head, huffman_table)
	print(x)
main()
