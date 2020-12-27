#!/usr/bin/python

import string
import sys
import re

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

for tile in tiles:
	l = ""
	r = ""
	for v in range(1,side + 1):
		l += tile[v][0]
		r += tile[v][side - 1]
	edges = []
	edges.append(edgesig(tile[1]))
	edges.append(edgesig(r))
	edges.append(edgesig(tile[side]))
	edges.append(edgesig(l))
	tile.append(edges)
	edges2 = []
	for e in edges:
		e2 = bitrev(e, 10)
		if e2 > e:
			e2 = e
		edges2.append(e2)
		if e2 in edgehist:
			edgehist[e2] += 1
		else:
			edgehist[e2] = 1
	tile.append(edges2)

corners = []
corner_product = 1
for tile in tiles:
	unique = 0
	edges = tile[side + 2]
	for e in edges:
		if edgehist[e] == 1:
			unique += 1
	if unique == 2:
		corners.append(tile)
		corner_product *= tile[0]

print("Part 1 answer: %d" % corner_product)

# Pick a corner, orient it so that right and down are unique
topleft = None
#for corner in corners:
#	if edgehist[corner[
print("Part 2 answer: %d" % 0)
