#!/usr/bin/python

import string
import sys

def fold_x(dots, fold):
	newdots = []
	for (x,y) in dots:
		if x > fold:
			x = fold * 2 - x
		if not (x,y) in newdots:
			newdots.append((x, y))
	return newdots

def fold_y(dots, fold):
	newdots = []
	for (x,y) in dots:
		if y > fold:
			y = fold * 2 - y
		if not (x,y) in newdots:
			newdots.append((x, y))
	return newdots

def show_dots(dots):
	width = max(x for (x,y) in dots) + 1
	height = max(y for (x,y) in dots) + 1
	for y in range(height):
		line = ''
		for x in range(width):
			if (x,y) in dots:
				line += '#'
			else:
				line += '.'
		print(line)
	print('')

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

dots = []

for line in fh:
	line = line.rstrip()
	if line == "":
		break
	(x,y) = line.split(',')
	dots.append((int(x),int(y)))

count1 = 0
for line in fh:
	line = line.rstrip()
	(instruction, position) = line.split('=')
	axis = instruction[-1]
	position = int(position)
	print('Fold %s at %d' % (axis, position))
	if axis == 'x':
		dots = fold_x(dots, position)
	else:
		dots = fold_y(dots, position)
	if count1 == 0:
		count1 = len(dots)

print('Part 1 answer: %d' % (count1))

print('Part 2 answer:')
show_dots(dots)
