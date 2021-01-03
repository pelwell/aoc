#!/usr/bin/python

import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r')

dir_re = re.compile(r'^([NSEWRLF])(\d+)')

north = 0
east = 0
heading = 0
ship_north = 0
ship_east = 0
way_north = 1
way_east = 10

for line in fh:
	m = dir_re.match(line)
	if m:
		dir = m.group(1)
		steps = int(m.group(2))
		movedir = dir
		rotate = 0
		way_steps = 0
		if dir == 'L':
			rotate = steps
		elif dir == 'R':
			rotate = 360-steps
		elif dir == 'F':
			movedir = 'ENWS'[heading/90]
			ship_north += way_north * steps
			ship_east += way_east * steps
		else:
			way_steps = steps
		if rotate:
			heading = (heading + rotate) % 360
			prev_east = way_east
			prev_north = way_north
			if rotate == 90:
				way_east = -prev_north
				way_north = prev_east
			elif rotate == 180:
				way_east = -prev_east
				way_north = -prev_north
			elif rotate == 270:
				way_east = prev_north
				way_north = -prev_east
		if movedir == 'N':
			north += steps
			way_north += way_steps
		elif movedir == 'S':
			north -= steps
			way_north -= way_steps
		elif movedir == 'E':
			east += steps
			way_east += way_steps
		elif movedir == 'W':
			east -= steps
			way_east -= way_steps

print("Part 1 answer: %d" % (abs(north) + abs(east)))
print("Part 2 answer: %d" % (abs(ship_north) + abs(ship_east)))
