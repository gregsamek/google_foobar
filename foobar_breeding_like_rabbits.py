"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence like all good rabbits do, the zombit population changes according to this bizarre formula, where R(n) is the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be equal to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"
"""

# memo starts with the known values already added
memo = {0: 1, 1: 1, 2: 2}

def is_even(number):
	'''
	Checks if number is even

	As you will see below, a completely different
	approach is needed for odd and even values of n
	'''
	if number % 2 == 0:
		return True
	else:
		return False

def R_func(x):
	'''Takes in a number x and returns R(x)

	searches memo to see if already calculated. if not already called, uses recursion to compute and update memo. Which recursive call is made depends on whether x is even or odd.
	'''
	if x in memo:
		return memo[x]

	if is_even(x):
		n = x / 2
		memo[x] = R_func(n) + R_func(n + 1) + n
		return memo[x]

	else:
		n = (x - 1) / 2
		memo[x] = R_func(n - 1) + R_func(n) + 1
		return memo[x]

def binary_search(left, right, target, odd):
	'''
	Recursive binary search for value of n that results in S

	My first implementation of this program did not include a 
	binary search. This proved impractical for large values of S
	and exceeded the maximum memory requirements. The trick to note
	here is that even and odd searches must be treated completely
	separately because they grow at different rates. In other words,
	the set R(n) for all values of n is not 'sorted'. The set R(n) 
	for all even numbers IS sorted, ascending.
	'''
	if left >= right:
		return None
	n = (right + left) / 2
	
	# even / odd correction
	if odd:
		if is_even(n):
			n += 1
	else:
		if not is_even(n):
			n += 1
	
	# checking the guess and adjusting the search constraints
	guess = R_func(n)
	if guess == target:
		return str(n)
	elif guess > target:
		right = n - 1
	elif guess < target:
		left = n + 1
	
	return binary_search(left, right, target, odd)

def answer(str_S):
	'''
	Takes a value of S and returns largest corresponding value of n

	We must treat R(n) separtely for even and odd values of n (see above explanation).
	We check odd values first because S increases at a slower rate. In other 
	words, if we find a valid value of n that is odd, there will never be a valid 
	even number of n that is larger.
	'''
	int_S = int(str_S)
	return binary_search(0, int_S+1, int_S, True) or binary_search(0, int_S, int_S, False)

# for i in range(0, 20):
# 	print "S = ", i, "n = ", answer(i)

# evens = []
# odds = []
# for i in range(2, 100, 2):
# 	evens.append(answer(i))
# for i in range(3, 100, 2):
# 	odds.append(answer(i))

# for i in evens:
# 	if i in odds:
# 		print "uh oh!", i

# print memo









































