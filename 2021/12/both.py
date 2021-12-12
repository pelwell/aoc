#!/usr/bin/python

import string
import sys

def findcount(s, m):
	return sum(1 if i == m else 0 for i in s)

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

edges = {}

for line in fh:
	(src, dst) = line.rstrip().split('-')

	dests = edges.get(src, [])
	if dests == []:
		edges[src] = dests
	if dst in dests:
		error('Duplicate link: %s - %s' % (src, dst))
	dests.append(dst)
	dests = edges.get(dst, [])
	if dests == []:
		edges[dst] = dests
	if src in dests:
		error('Duplicate link: %s - %s' % (src, dst))
	dests.append(src)

active = [['start']]
paths = []

while active:
	nextactive = []
	for path in active:
		pos = path[-1]
		if pos == 'end':
			paths.append(path)
			continue
		for nextpos in edges[pos]:
			if nextpos.islower() and nextpos in path:
				continue
			nextactive.append(path + [nextpos])
	active = nextactive

print("Part 1 answer: %d" % (len(paths)))

active = [ (None, ['start'])]
paths = []

while active:
	nextactive = []
	for (dup, path) in active:
		pos = path[-1]
		if pos == 'end':
			paths.append(path)
			continue
		for nextpos in edges[pos]:
			if nextpos.islower() and nextpos in path:
				if nextpos == 'start':
					continue
				if dup != None:
					continue
				nextactive.append((nextpos, path + [nextpos]))
			else:
				nextactive.append((dup, path + [nextpos]))
	active = nextactive

print("Part 2 answer: %d" % (len(paths)))
