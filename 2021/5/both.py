#!/usr/bin/python

import string
import sys
import re

def sgn(n):
	return 1 if n > 0 else -1 if n < 0 else 0

def plot(map, x, y):
	point = str(x) + ',' + str(y)
	if point in map:
		map[point] += 1
	else:
		map[point] = 1

def draw_line(map, x, y, x2, y2, diags):
	dx = sgn(x2 - x)
	dy = sgn(y2 - y)
	if not diags and dx and dy:
		return
	steps = max(abs(x2 - x), abs(y2 - y)) + 1
	for i in range(steps):
		plot(map, x, y)
		x += dx
		y += dy

def show_map(map):
	width = 0
	height = 0
	for point in map:
		nums = point.split(',')
		x = int(nums[0])
		y = int(nums[1])
		width = max(x + 1, width)
		height = max(y + 1, height)
	print('Size %dx%d:' % (width, height))
	for y in range(height):
		row = ''
		for x in range(width):
			point = str(x) + ',' + str(y)
			if point in map:
				row += str(map[point])
			else:
				row += '.'
		print(row)
	print('')

def count_crossings(map):
	return sum(1 if value > 1 else 0 for value in map.values())

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');
map_re = re.compile(r"^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)$")

map1 = {}
map2 = {}
	
for line in fh:
	line = line.rstrip()
	m = map_re.match(line)
	if m:
		draw_line(map1, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), False)
		draw_line(map2, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), True)

print("Part 1 answer: %d" % (count_crossings(map1)))
print("Part 2 answer: %d" % (count_crossings(map2)))
