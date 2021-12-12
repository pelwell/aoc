#!/usr/bin/python

import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

pos = 0
count1 = 0
count2 = 0
window = [ 0, 0, 0 ]

for line in fh:
	line = line.rstrip()
	num = int(line)
	if pos > 0 and num > window[(pos - 1) % 3]:
		count1 += 1
	if pos > 2 and num > window[pos % 3]:
		count2 += 1
	window[pos % 3] = num
	pos += 1

print("Part 1 answer: %d" % count1)
print("Part 2 answer: %d" % count2)
