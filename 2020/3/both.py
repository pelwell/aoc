#!/usr/bin/python

import re
import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

map_re = re.compile(r"^([\.#]+)\s*$")

map = []

for line in fh:
	m = map_re.match(line)
	if m:
		map.append(m.group(1))

def count_trees(map, dx, dy):
	width = len(map[0])
	height = len(map)
	trees = 0
	x = 0
	y = 0
	while True:
		x += dx
		y += dy
		if y >= height:
			break
		if map[y][x % width] == '#':
			trees += 1
	return trees

answer = count_trees(map, 3, 1)

print("Part 1 answer: %d" % answer)

answer *= count_trees(map, 1, 1)
answer *= count_trees(map, 5, 1)
answer *= count_trees(map, 7, 1)
answer *= count_trees(map, 1, 2)

print("Part 2 answer: %d" % answer)
