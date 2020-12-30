#!/usr/bin/python

import string
import sys

# newcube is active if oldtile is active with 2 or 3 neighbours
#               or if oldtile is inactive with 3 neighbours

dirs = []
dirs2 = []

def generation(map):
	inactive_nbrs = {}
	newmap = {}
	for pos in map.values():
		neighbours = 0
		for dir in dirs:
			tryx = pos[0] + dir[0]
			tryy = pos[1] + dir[1]
			tryz = pos[2] + dir[2]
			trypos = "%d,%d,%d" % (tryx, tryy, tryz)
			if map.has_key(trypos):
				neighbours += 1
			else:
				inactive_nbrs[trypos] = inactive_nbrs.get(trypos, 0) + 1
		if neighbours == 2 or neighbours == 3:
			newmap["%d,%d,%d" % (pos[0], pos[1], pos[2])] = pos
	for item in inactive_nbrs.items():
		if item[1] == 3:
			nums = item[0].split(',')
			newmap[item[0]] = [ int(nums[0]), int(nums[1]), int(nums[2]) ]

	return newmap

def generation2(map):
	inactive_nbrs = {}
	newmap = {}
	for pos in map.values():
		neighbours = 0
		for dir in dirs2:
			tryx = pos[0] + dir[0]
			tryy = pos[1] + dir[1]
			tryz = pos[2] + dir[2]
			tryw = pos[3] + dir[3]
			trypos = "%d,%d,%d,%d" % (tryx, tryy, tryz, tryw)
			if map.has_key(trypos):
				neighbours += 1
			else:
				inactive_nbrs[trypos] = inactive_nbrs.get(trypos, 0) + 1
		if neighbours == 2 or neighbours == 3:
			newmap["%d,%d,%d,%d" % (pos[0], pos[1], pos[2], pos[3])] = pos
	for item in inactive_nbrs.items():
		if item[1] == 3:
			nums = item[0].split(',')
			newmap[item[0]] = [ int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]) ]

	return newmap

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

map = {}
map2 = {}

y = 0
for line in fh:
	row = line.rstrip()
	for x in range(len(row)):
		if row[x] == '#':
			map["%d,%d,%d" % (x, y, 0)] = (x, y, 0)
			map2["%d,%d,%d,%d" % (x, y, 0, 0)] = (x, y, 0, 0)
	y += 1

for x in range(-1,2):
	for y in range(-1,2):
		for z in range(-1,2):
			if x or y or z:
				dirs.append((x,y,z))
			for w in range(-1, 2):
				if x or y or z or w:
					dirs2.append((x,y,z,w))

for tick in range(6):
	map = generation(map)

print("Part 1 answer: %d" % len(map.keys()))

for tick in range(6):
	map2 = generation2(map2)

print("Part 2 answer: %d" % len(map2.keys()))
