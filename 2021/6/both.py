#!/usr/bin/python

import string
import sys
import re

MAX = 9

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

counts = [0] * MAX

for line in fh:
	for n in line.rstrip().split(','):
		counts[int(n)] += 1

for i in range(80):
	counts[(i - 2) % MAX] += counts[i % MAX]

print("Part 1 answer: %d" % (sum(counts)))

for i in range(80,256):
	counts[(i - 2) % MAX] += counts[i % MAX]

print("Part 2 answer: %d" % (sum(counts)))
