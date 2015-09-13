"""
Spy snippets
============

You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the tool called "Snippet Search." While you really wanted to tell him how such a feature is a waste of time in this intense, fast-paced spy organization, you also wouldn't mind getting kudos from a leader. How hard could it be, anyway?

When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short snippet of the page containing the terms that were searched for. 

Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all of the given search terms. The search terms can appear in any order.

The length of a snippet is the number of words in the snippet. For example, the length of the snippet "round fluffy rabbit tails" is 4. (Hey, don't judge your colleagues for what they search in their spare time).

The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be separated by a single space. A word could appear multiple times in the document.
searchTerms will be a list of words, each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.

Search terms must match words exactly, so "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello hello where world" and the search terms are ["hello", "world"], you must return "world there hello".

The document will be guaranteed to contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters long. Repeat words in the document are considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10 letters long.

Python
======

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Test cases
==========

Inputs:
    (string) document = "many google employees can program"
    (string list) searchTerms = ["google", "program"]
Output:
    (string) "google employees can program"

Inputs:
    (string) document = "a b c d a"
    (string list) searchTerms = ["a", "c", "d"]
Output:
    (string) "c d a" 
"""

def answer(document, searchTerms):
	doc_list = document.split()
	doc_len = len(doc_list)
	search_len = len(searchTerms)
	
	hit_list = []
	for i in range(doc_len):
		for j in range(search_len):
			if doc_list[i] == searchTerms[j]:
				hit_list.append(i)
				break

	left = min(hit_list)
	right = max(hit_list)
	best_left = left
	best_right = right
	length = len(doc_list[left:right+1])
	final_list = []

	for i in range(left, right + 1):
		for j in range(i + 1, right + 1):
			if all_in(i, j, doc_list, searchTerms):
				if len(doc_list[i:j + 1]) < length:
					length = len(doc_list[i:j + 1])
					best_left = i
					best_right = j
					if length == search_len:
						final_list = doc_list[best_left:best_right + 1]
	final_list = doc_list[best_left:best_right + 1]
	result = " "
	return result.join(final_list)

def all_in(start, stop, doc, search_list):
	for each in search_list:
		if each not in doc[start:stop + 1]:
			return False
	return True

print answer("a b a d c", ["c"])
print answer("many google employees can program", ["google", "program"])
print answer("a b c d a", ["a", "c", "d"])
print answer("c d a b a", ["a", "c", "d"])
print answer("many google employees can program can google employees because google is a technology company that writes programs",["google", "program", "can"])
print answer("a b d a c a c c d a", ["a", "c", "d"])

# change_made = 1
	# while change_made:
	# 	change_made = 0	
	# 	for i in graph:
	# 		if left in i:
	# 			for j in i:
	# 				if j > left:
	# 					left = j
	# 					change_made = 1
	# 		if right in i:
	# 			for j in i:
	# 				if j < right:
	# 					right = j
	# 					change_made = 1

	# test_list = doc_list[left:right+1]
	# valid_snip = 1
	# while valid_snip == 1:
	# 	for i in searchTerms:
	# 		if i not in test_list:
	# 			valid_snip = 0
	# 	if valid_snip == 1:
	# 		right -= 1
	# 		test_list = doc_list[left:right+1]
	# right += 1
	# test_list = doc_list[left:right+1]
	# print "after trim from right: ", test_list
	# valid_snip = 1
	# while valid_snip == 1:
	# 	for i in searchTerms:
	# 		if i not in test_list:
	# 			valid_snip = 0
	# 	if valid_snip == 1:
	# 		left += 1
	# 		test_list = doc_list[left:right+1]
	# left -= 1
	# test_list = doc_list[left:right+1]
	# print "after trim from left: ", test_list
	# doc_list = doc_list[left:right+1]
	# result = ""
	# for i in doc_list:
	# 	result = result + i + " "
	# return result.rstrip()





































