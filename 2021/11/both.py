#!/usr/bin/python

import string
import sys

offsets = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

width = 0
height = 0

def show_map(map):
	for y in range(height):
		row = map[y]
		s = ''
		for x in range(width):
			v = row[x]
			if v <= 9:
				s += str(v)
			else:
				s += '*'
		print(s)
	print('')


def run_step(map):
	for y in range(height):
		row = map[y]
		for x in range(width):
			row[x] += 1
	flashes = 0
	while True:
		new_flashes = 0
		for y in range(height):
			row = map[y]
			for x in range(width):
				if row[x] == 10:
					new_flashes += 1
					row[x] = 0
					for dx, dy in offsets:
						if x + dx < 0 or x + dx >= width:
							continue
						if y + dy < 0 or y + dy >= height:
							continue
						v = map[y+dy][x+dx]
						if v > 0 and v < 10:
							map[y+dy][x+dx] = v + 1
		if not new_flashes:
			break
		flashes += new_flashes
	return flashes

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

map = []
for line in fh:
	map.append([int(c) for c in line.rstrip()])
height = len(map)
width = len(map[0])

flashes = 0

for i in range(100):
	flashes += run_step(map)

print("Part 1 answer: %d" % (flashes))

for i in range(101,100000):
	flashes = run_step(map)
	if flashes == width*height:
		break

print("Part 2 answer: %d" % (i))
