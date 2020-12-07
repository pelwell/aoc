#!/usr/bin/python

import string
import sys

def sum_to(arr, list, sum):
	for val in list:
		if (val < sum) and arr[sum - val]:
			return (val, sum - val)
	return None

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

arr = [ False ] * 2020
list = []

for line in fh:
	line = line.rstrip()
	num = int(line)
	list.append(num)
	arr[num] = True

found = sum_to(arr, list, 2020)
print("Part 1 answer: %d" % (found[0] * found[1]))

for num in list:
	found2 = sum_to(arr, list, 2020 - num)
	if found2 != None:
		found = [num, found2[0], found2[1]]
		break

print("Part 2 answer: %d" % (found[0] * found[1] * found[2]))
