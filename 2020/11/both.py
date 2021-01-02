#!/usr/bin/python

import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r')

stride = 0
rows = 0
map = ''

for line in fh:
	map += ' ' + line.rstrip()
	rows += 1
	if not stride:
		stride = len(map)

blank = ' ' * stride
map = blank + map + blank + ' '
map2 = map

def print_map(map):
	for x in map.split():
		print(x)
	print

def generation(map):
	newmap = ""
	for pos in range(len(map)):
		c = map[pos]
		near = map[(pos - stride - 1) : (pos - stride + 2)]
		near += map[(pos - 1) : (pos + 2)]
		near += map[pos + stride - 1: pos + stride + 2]
		if c == 'L' and near.count('#') == 0:
			c = '#'
		elif c == '#' and near.count('#') >= 5:
			c = 'L'
		newmap += c

	return newmap

def generation2(map):
	newmap = ""
	dirs = (-stride - 1, -stride, -stride + 1,
	        -1, 1,
	        stride - 1, stride, stride + 1)

	for pos in range(len(map)): 
 		count = 0
 		atpos = 0
 		c = map[pos]
 		if c != ' ':
	 		for dir in dirs:
 				scanpos = pos
 				while True:
 					scanpos += dir
 					atpos = map[scanpos]
 					if atpos != '.':
 						break
 				if atpos == '#':
 					count += 1
 		if c == 'L' and count == 0:
 			c = '#'
 		elif c == '#' and count >= 5:
 			c = 'L'
		newmap += c

	return newmap

while True:
	newmap = generation(map)
	if newmap == map:
		break
	map = newmap

answer1 = map.count('#')
print("Part 1 answer: %d" % answer1)

while True:
	newmap = generation2(map2)
	if newmap == map2:
		break
	map2 = newmap

answer2 = map2.count('#')

print("Part 2 answer: %d" % answer2)
