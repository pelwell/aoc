#!/usr/bin/python

import string
import sys

def generation(map):
	for layer in range(len(map)):
		if 

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

map = []

for line in fh:
	map.append(line.rstrip())


map = [ map ]

for tick in range(6):
	newmap = generation(map)

print("Part 1 answer: %d" % alive)
print("Part 2 answer: %d" % product)
