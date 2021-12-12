#!/usr/bin/python

import string
import sys

def try_pos(map, x, y, h, bh, nf):
	ph = map[y][x]
	if ph > h and ph < 9:
		nf.append((x, y, ph))
		map[y][x] = bh

def measure_basin(map, x, y):
	basin_height = map[y][x]
	frontier = [(x, y, basin_height)]
	size = 0
	while frontier:
		size += len(frontier)
		next_frontier = []
		for (x,y,h) in frontier:
			if h >= 9:
				continue
			try_pos(map, x, y-1, h, basin_height, next_frontier)
			try_pos(map, x, y+1, h, basin_height, next_frontier)
			try_pos(map, x-1, y, h, basin_height, next_frontier)
			try_pos(map, x+1, y, h, basin_height, next_frontier)
		frontier = next_frontier
	return size

def show_map(map):
	for row in map:
		s = ''
		for h in row:
			s += str(h) if h < 10 else '#'
		print(s)

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

score1 = 0

row = None

rows = []

width = 0
for line in fh:
	row = [10] + [int(c) for c in line.rstrip()] + [10]
	if width == 0:
		width = len(row)
		border = [10] * width
		rows.append(border)
	rows.append(row)
rows.append(border)
height = len(rows)

basin_sizes = []

for y in range(1, height - 1):
	top = rows[y - 1]
	mid = rows[y]
	bot = rows[y + 1]
	for x in range(1, width - 1):
		v = mid[x]
		if v < top[x] and v < bot[x] and v < mid[x - 1] and v < mid[x + 1]:
			score1 += v + 1
			basin_sizes.append(measure_basin(rows, x, y))

print("Part 1 answer: %d" % (score1))

basin_sizes.sort()

print("Part 2 answer: %d" % (basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]))
