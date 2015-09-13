'''Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
'''

from math import factorial

class Node:

	def __init__(self, data):
		'''
		Initializes node with three attributes: the value of the node
		itself, plus two additional children nodes
		'''
		self.value = data
		self.left_child = None
		self.right_child = None

	def insert(self, data):
		'''
		Traverses the tree searching for the location to insert the new node
		'''
		if self.value == data:
			pass
		elif self.value > data:
			if self.left_child:
				self.left_child.insert(data)
			else:
				self.left_child = Node(data)
		else:
			if self.right_child:
				self.right_child.insert(data)
			else:
				self.right_child = Node(data)

class Tree:

	def __init__(self):
		'''
		I could have implemented this program with only the node class,
		and this would've saved a few lines of code, but to me it is more 
		intuitive to think of the tree and nodes as two separate classes
		'''
		self.root = None

	def insert(self, value):
		if self.root:
			return self.root.insert(value)
		else:
			self.root = Node(value)

def count_children(node):
	'''
	Counts the total number of children from a parent node
	'''
	if node:
		return 1 + count_children(node.left_child) + count_children(node.right_child)
	else:
		return 0

def combinations(n, k):
    """
    Returns the number of unique subsets of 'k' number of elements
    that can be chosen from a set of 'n' elements.

    Eg. combinations(3,2) = 3
    Unique subsets of size '2' that can be made from (1,2,3):
    (1,2), (1,3), (2, 3)

    Note: borrowed from line_up_the_captives.py
    """
    return factorial(n) / (factorial(k) * factorial(n - k))

def sequences(tree):
	'''
	Takes in an tree and returns the number of arrays that could be
	used to create this tree.

	This is the secret sauce of the program. The thought process here is that
	for each parent we can look at its left_children and right_children
	counts and calculate the number of ways we could seleft right_children
	from the total pool of children.

	We must then recursively analyze each direct child and its children.
	Because this is a combinatorics computation, note that we are multiplying
	by the recursive calls, not simply adding them.
	'''
	# This is our base case for when we reach the end of each 'branch'
	if not tree:
		return 1

	# How many different ways can the 
	left_children = count_children(tree.left_child)
	right_children = count_children(tree.right_child)
	temp = combinations(left_children + right_children, right_children)

	return temp * sequences(tree.left_child) * sequences(tree.right_child)

def answer(seq):
	'''
	Creates the binary tree from the input array and calls the 
	sequences function on this tree
	'''
	bst = Tree()
	for i in seq:
		bst.insert(i)
	return sequences(bst.root)

print answer([2, 3, 1])
print answer([5, 9, 8, 2, 1])
print answer([1, 2, 3, 4, 5])







































