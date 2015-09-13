"""Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight, and so on. Each string is one of: 

"L" : put weight on left-hand side 
"R" : put weight on right-hand side 
"-" : do not use weight 

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1,000,000,000.

Python
======

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Test cases
==========

Inputs:
    (int) x = 2
Output:
    (string list) ["L", "R"]

Inputs:
    (int) x = 8
Output:
    (string list) ["L", "-", "R"]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder."""

def ternary_converter(decimal):
	if decimal == 0:
		return 0
	exp = 0
	result = []
	while decimal >= 3 ** exp:
		result.append(0)
		exp += 1
	exp -= 1
	quotient = decimal
	while exp >= 0:
		result[exp] = quotient % 3
		quotient = quotient / 3
		exp -= 1
	return result

def balance(ternary):
	ternary.reverse()
	carry = 0
	temp = 0
	for i in range(len(ternary)):
		temp = ternary[i] + carry
		if temp == 3:
			ternary[i] = "-"
			carry = 1
		elif temp == 2:
			ternary[i] = "L"
			carry = 1
		elif temp == 1:
			ternary[i] = "R"
			carry = 0
		elif temp == 0:
			ternary[i] = "-"
			carry = 0
	if carry == 1:
		ternary.append("R")
	return ternary

def answer(x):
	return balance(ternary_converter(x))

for i in range(1,18):
	print i, " = ", answer(i) 

	# step_one = []
	# for i in range(len(ternary)):
	# 	temp = ternary[i] + 1 + carry
	# 	if temp > 2:
	# 		step_one.append(0)
	# 		carry = 1
	# 	else:
	# 		step_one.append(temp)
	# 		carry = 0
	# return step_one










































