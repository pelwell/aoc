#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');
map_re = re.compile(r"^([a-z]+) ([0-9]+)$")

distance = 0
depth1 = 0
depth2 = 0
aim = 0
	
for line in fh:
	line = line.rstrip()
	m = map_re.match(line)
	if m:
		dir = m.group(1)
		d = int(m.group(2))
		if dir == "forward":
			distance += d 
			depth2 += aim * d
		elif dir == "up":
			depth1 -= d
			aim -= d
		elif dir == "down":
			depth1 += d
			aim += d

print("Part 1 answer: %d" % (depth1 * distance))
print("Part 2 answer: %d" % (depth2 * distance))
