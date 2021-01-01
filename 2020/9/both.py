#!/usr/bin/python

import sys;
import re;

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

list = [int(x.rstrip()) for x in fh]

preamble_len = 25
if len(sys.argv) > 1:
	preamble_len = 5

def find_pair_with_sum(sum, arr):
	arr = arr[:]
	arr.sort()
	i = 0
	j = len(arr) - 1
	while i < j:
		pairsum = arr[i] + arr[j]
		if pairsum == sum:
			return 1
		if pairsum > sum:
			j -= 1
		else:
			i += 1
	return 0

answer1 = 0

for pos in range(preamble_len, len(list)):
	if not find_pair_with_sum(list[pos], list[pos - preamble_len:pos]):
		answer1 = list[pos]
		break

print("Part 1 answer: %d" % answer1)

answer2 = 0
i = 0
j = 1
sum = list[i] + list[j]

while i < len(list) - 1:
	if sum == answer1:
		sublist = list[i:j+1]
		sublist.sort()
		answer2 = sublist[0] + sublist[-1]
		break
	elif sum > answer1:
		sum -= list[i]
		i += 1
	else:
		j += 1
		sum += list[j]

print("Part 2 answer: %d" % answer2)
