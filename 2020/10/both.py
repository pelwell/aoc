#!/usr/bin/python

import sys;
import re;

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

list = [int(x.rstrip()) for x in fh]
list.sort()

hist = [ 0 ] * 5
last = 0
onediffcount = 0

count = 1
runmult = (1, 1, 2, 4, 7)

for jolts in list:
	diff = jolts - last
	hist[diff] += 1
	if diff == 1:
		onediffcount += 1
	elif onediffcount:
		count *= runmult[onediffcount];
		onediffcount = 0
	last = jolts

count *= runmult[onediffcount]

hist[3] += 1

print("Part 1 answer: %d" % (hist[1]*hist[3]))
print("Part 2 answer: %d" % count)
