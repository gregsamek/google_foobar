'''Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token on the left-most square and rolls a special three-sided die. 

If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently. If there is no square to the left, the game is invalid, and you start again.

If the die rolls a "Stay", the token stays where it is. 

If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently. If there is no square to the right, the game is invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the rightmost square before t rolls are done then the only valid dice roll is to roll a "Stay". If you roll anything else, the game is invalid (i.e., you cannot move left or right from the rightmost square).

To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the game he just played: the sequence of dice rolls. If some minion has already submitted the exact same sequence, they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable. 

Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker, you are interested in knowing the maximum possible size a leaderboard can have.

Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) t = 1
    (int) n = 2
Output:
    (int) 1

Inputs:
    (int) t = 3
    (int) n = 2
Output:
    (int) 3
'''
def answer(t, n):
    '''
    Returns the number of playable games given a board of size n and t rolls
    '''
    board_1, board_2 = [0]*n, [0]*n
    board_1[0] = 1
    
    for i in xrange(t):
        board_1, board_2 = board_2, board_1
        
        for j in xrange(n):
            '''
            The number of games possible for this (t,n) is
            the sum of the possible games after each legal roll:
            1) dice roll "left" (if not on the leftmost board space)
            2) dice roll "stay"
            3) dice roll "right" (if not on the rightmost board space)
            '''
            board_1[j] =\
            (j > 0 and board_2[j - 1]) +\
            board_2[j] +\
            (j + 1 < n - 1 and board_2[j + 1])
    
    # using modulo as instructed
    return board_1[n-1] % 123454321

# print answer(2, 3) #1
# print answer(1, 2) #1
# print answer(3, 2) #3
# print answer(20, 5) #19535230
t, n = 5, 6
for i in range(1, t+1):
	for j in range(2, n+1):
		print 't: ', i, 'n: ', j, 'ans: ', answer(i, j)
















































