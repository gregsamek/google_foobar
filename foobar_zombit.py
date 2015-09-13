"""Zombit antidote
===============

Forget flu season. Zombie rabbits have broken loose and are terrorizing Silicon Valley residents! Luckily, you've managed to steal a zombie antidote and set up a makeshift rabbit rescue station. Anyone who catches a zombie rabbit can schedule a meeting at your station to have it injected with the antidote, turning it back from a zombit to a fluffy bunny. Unfortunately, you have a limited amount of time each day, so you need to maximize these meetings. Every morning, you get a list of requested injection meetings, and you have to decide which to attend fully. If you go to an injection meeting, you will join it exactly at the start of the meeting, and only leave exactly at the end.

Can you optimize your meeting schedule? The world needs your help!

Write a method called answer(meetings) which, given a list of meeting requests, returns the maximum number of non-overlapping meetings that can be scheduled. If the start time of one meeting is the same as the end time of another, they are not considered overlapping.

meetings will be a list of lists. Each element of the meetings list will be a two element list denoting a meeting request. The first element of that list will be the start time and the second element will be the end time of that meeting request.

All the start and end times will be non-negative integers, no larger than 1000000. 
The start time of a meeting will always be less than the end time.

The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.

Test cases
==========

Inputs:
    (int) meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
Output:
    (int) 4

Inputs:
    (int) meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
Output:
    (int) 1

Python Constraints
==================

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
"""

# Greg's Notes
# This is a scheduling problem
# input: list of meeting requests with stop and start time
# output: max number of non-overlapping mtgs that can be scheduled
# The list of requests will be ordered randomly

from operator import itemgetter # allows me to easily sort by finishing time

def answer(meetings):
	meetings.sort(key=itemgetter(1)) # sort requests by earliest finish time
	schedule = [meetings[0]]
	reference = meetings.pop(0)
	for request in range(len(meetings)):
		for request in meetings:
			if request[0] < reference[1]: # if next request starts before reference finishes
				x = 1
			else:
				schedule.append(request) # add to schedule
				reference = request
	return len(schedule)

# print answer([[2, 3], [5, 6], [1, 2], [9, 10]]) # 4
# print answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]) # 4
# print answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]]) # 1

# meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
# print "Expected 4. Actual: " + str(answer(meetings))
# meetings = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
# print "Expected 5. Actual: " + str(answer(meetings))
# meetings = [[0, 1], [0, 2], [2, 3], [3, 4], [4, 5]]
# print "Expected 4. Actual: " + str(answer(meetings))

# meetings = [[0, 1], [1, 2], [0, 3], [3, 4], [4, 5]]
# print "Expected 4. Actual: " + str(answer(meetings))

# meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
# print "Expected 1. Actual: " + str(answer(meetings))
# meetings = [[7,12], [1,3], [8,9], [15,17], [3,8], [11,16]]
# print "Expected 4. Actual: " + str(answer(meetings))







































