#!/usr/bin/python

import string
import sys
import re

# newtile is black if oldtile is black with 1 or 2 neighbours
#               or if oldtile is white with 2 neighbours

def generation(map):
	white_nbrs = {}
	newmap = {}
	for pos in map.values():
		neighbours = 0
		for dir in [ (1, 1), (-1, 1), (1, -1), (-1, -1), (2, 0), (-2, 0) ]:
			tryx = pos[0] + dir[0]
			tryy = pos[1] + dir[1]
			trypos = "%d,%d" % (tryx, tryy)
			if map.has_key(trypos):
				neighbours += 1
			else:
				white_nbrs[trypos] = white_nbrs.get(trypos, 0) + 1
		if neighbours == 1 or neighbours == 2:
			newmap["%d,%d" % (pos[0], pos[1])] = pos
	for item in white_nbrs.items():
		if item[1] == 2:
			nums = item[0].split(',')
			newmap[item[0]] = [ int(nums[0]), int(nums[1]) ]

	return newmap

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

map = {}

for line in fh:
	line = line.rstrip()
	xpos = 0
	ypos = 0
	for dir in re.findall(r'(ne|nw|se|sw|e|w)', line):
		if dir == 'ne':
			xpos += 1
			ypos += 1
		elif dir == 'nw':
			xpos -= 1
			ypos += 1
		elif dir == 'se':
			xpos += 1
			ypos -= 1
		elif dir == 'sw':
			xpos -= 1
			ypos -= 1
		elif dir == 'e':
			xpos += 2
		elif dir == 'w':
			xpos -= 2
	pos = "%d,%d" % (xpos, ypos)
	if map.has_key(pos):
		del map[pos]
	else:
		map[pos] = (xpos, ypos)

print("Part 1 answer: %d" % len(map.keys()))

for i in range(100):
	map = generation(map)

print("Part 2 answer: %d" % len(map.keys()))
