#!/usr/bin/python

import string
import sys
import re
import math

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

hdr_re = re.compile(r'^Tile (\d+):')
row_re = re.compile(r'^([\.#]+)')

def edgesig(str):
	num = 0
	for c in str:
		num *= 2
		if c == '#':
			num += 1
	return num

def bitrev(n, l):
	n2 = 0
	for i in range(l):
		n2 <<= 1
		if n & (1 << i):
			n2 += 1
	return n2

side = 10
tiles = []

for line in fh:
	m1 = hdr_re.match(line)
	m2 = row_re.match(line)
	if m1:
		tile = [ int(m1.group(1)) ]
		tiles.append(tile)
	elif m2:
		tile.append(m2.group(1))

edgehist = {}

left = 0
top = 1
right = 2
bottom = 3

size = 0

def print_tile(tile):
	for row in range(side):
		print("".join(tile[1 + row]))

def vflip(tile):
	for i in range(1,6):
		tmp = tile[i]
		tile[i] = tile[11-i]
		tile[11-i] = tmp
	tmp = tile[11][top]
	tile[11][top] = tile[11][bottom]
	tile[11][bottom] = tmp
	tile[11][left] = bitrev(tile[11][left], 10)
	tile[11][right] = bitrev(tile[11][right], 10)
	tmp = tile[12][top]
	tile[12][top] = tile[12][bottom]
	tile[12][bottom] = tmp

def hflip(tile):
	rotate_anti(tile)
	vflip(tile)
	rotate_anti(tile)
	rotate_anti(tile)
	rotate_anti(tile)

def rotate_anti(tile):
	# print("Tile %d before: %d %d %d %d (%d %d %d %d)" % (tile[0], tile[11][top], tile[11][right], tile[11][bottom], tile[11][left], tile[12][top], tile[12][right], tile[12][bottom], tile[12][left]))
	# print_tile(tile)
	tmp = tile[11][top]
	tile[11][top] = tile[11][right]
	tile[11][right] = bitrev(tile[11][bottom], 10)
	tile[11][bottom] = tile[11][left]
	tile[11][left] = bitrev(tmp, 10)

	tmp = tile[12][top]
	tile[12][top] = tile[12][right]
	tile[12][right] = tile[12][bottom]
	tile[12][bottom] = tile[12][left]
	tile[12][left] = tmp

	new = []
	for y in range(10):
		row = []
		new.append(row)
		for x in range(10):
			row.append(tile[x + 1][side - 1 - y])
	tile[1:11] = new
	# print("Tile %d after: %d %d %d %d (%d %d %d %d)" % (tile[0], tile[11][top], tile[11][right], tile[11][bottom], tile[11][left], tile[12][top], tile[12][right], tile[12][bottom], tile[12][left]))
	# print_tile(tile)

def find_edge(sig, edge, neighbour):
	match = min(sig, bitrev(sig, 10))
	pair = edgehist[match]
	tile = pair[0]
	if tile == neighbour:
		tile = pair[1]
	rot = 0
	while match != tile[12][edge]:
		rot += 1
		rotate_anti(tile)
	if tile[11][edge] != sig:
		if edge == left or edge == right:
			vflip(tile)
		else:
			hflip(tile)
	# print("Tile %d found: %d %d %d %d (%d %d %d %d)" % (tile[0], tile[11][top], tile[11][right], tile[11][bottom], tile[11][left], tile[12][top], tile[12][right], tile[12][bottom], tile[12][left]))
	return tile

size = int(math.sqrt(len(tiles)))

for tile in tiles:
	l = ""
	r = ""
	for v in range(1,side + 1):
		l += tile[v][0]
		r += tile[v][side - 1]
	edges = [None] * 4
	edges[top] = edgesig(tile[1])
	edges[right] = edgesig(r)
	edges[bottom] = edgesig(tile[side])
	edges[left] = edgesig(l)
	tile.append(edges)
	edges2 = []
	for e in edges:
		e2 = min(e, bitrev(e, 10))
		edges2.append(e2)
		if e2 in edgehist:
			edgehist[e2].append(tile)
		else:
			edgehist[e2] = [tile]
	tile.append(edges2)
	# print("Tile %d: %d %d %d %d" % (tile[0], edges2[0], edges2[1], edges2[2], edges2[3]))

corners = []
corner_product = 1
for tile in tiles:
	unique = 0
	edges = tile[12]
	inner = []
	for e in edges:
		if len(edgehist[e]) == 1:
			unique += 1
		else:
			inner.append(e)
	if unique == 2:
		corners.append(tile)
		corner_product *= tile[0]
		# print("  Corner %d - %d %d" % (tile[0], inner[0], inner[1]))

print("Part 1 answer: %d" % corner_product)

grid = []

for y in range(size):
	grid.append([None] * size)
	for x in range(size):
		if x == 0 and y == 0:
			# Pick any corner
			tile = corners[0]
			edges = tile[12][:]
			# orient it so that left and top are unique
			while len(edgehist[edges[left]]) != 1 or len(edgehist[edges[top]]) != 1:
				rotate_anti(tile)
				edges = edges[1:] + edges[:1]
		elif x == 0:
			tile = find_edge(topsig, top, toptile)
		else:
			tile = find_edge(leftsig, left, lefttile)
		if x == 0:
			toptile = tile
			topsig = tile[11][bottom]
		lefttile = tile
		leftsig = tile[11][right]
		grid[y][x] = tile
		# print("%d,%d = %d (%d %d %d %d)" % (y, x, tile[0], tile[12][top], tile[12][right], tile[12][bottom], tile[12][left]))

print("Part 1 answer: %d" % (grid[0][0][0] * grid[0][size - 1][0] * grid[size - 1][0][0] * grid[size - 1][size - 1][0]))

side -= 2
map = []
for y in range(size):
	for row in range(side):
		line = []
		for x in range(size):
			line.extend(grid[y][x][2 + row][1:-1])
		map.append(line)

monster_width = 20
monster_height = 3

monster = [ (0,18), (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18),
            (1,19), (2,1), (2,4), (2,7), (2,10), (2,13), (2,16) ]

monsters = [ ]
for hflip in range(2):
	for vflip in range(2):
		mnstr = []
		for pos in monster:
			if hflip:
				xpos = monster_width - 1 - pos[1]
			else:
				xpos = pos[1]
			if vflip:
				ypos = monster_height - 1 - pos[0]
			else:
				ypos = pos[0]
			mnstr.append((ypos, xpos))
		monsters.append(mnstr)

def monster_hunt(map):
	size = len(map)
	for mnstr in monsters:
		for y in range(size - monster_height):
			for x in range(size - monster_width):
				count = 0
				for pos in mnstr:
					if map[y + pos[0]][x + pos[1]] == '.':
						break
					count += 1
				if count == len(mnstr):
					for pos in mnstr:
						map[y + pos[0]][x + pos[1]] = 'O'
				count = 0
				for pos in mnstr:
					if map[x + pos[1]][y + pos[0]] == '.':
						break
					count += 1
				if count == len(mnstr):
					for pos in mnstr:
						map[x + pos[1]][y + pos[0]] = 'O'

monster_hunt(map)

count = 0
size = len(map)
for y in range(size):
	for x in range(size):
		if map[y][x] == '#':
			count += 1

print("Part 2 answer: %d" % count)
