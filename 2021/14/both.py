#!/usr/bin/python

import string
import sys

def makepoly(s):
	poly = {}
	last = ' '
	for c in s:
		poly[last + c] = poly.get(last + c, 0) + 1
		last = c
	return poly

def polymerise(poly, rules):
	newpoly = {}
	for pair, count in poly.items():
		insert = rules.get(pair, None)
		if insert:
			newpoly[pair[0]+insert] = newpoly.get(pair[0]+insert, 0) + count
			newpoly[insert+pair[1]] = newpoly.get(insert+pair[1], 0) + count
		else:
			newpoly[pair] = newpoly.get(pair,0) + count
	return newpoly

def makehist(poly):
	hist = {}
	for pair, count in poly.items():
		c = pair[1]
		hist[c] = hist.get(c, 0) + count
	return hist

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

polymer = makepoly(fh.readline().rstrip())

fh.readline()

rules = {}

for line in fh:
	rules[line[:2]] = line[6]

for step in range(10):
	polymer = polymerise(polymer, rules)

hist = makehist(polymer)
freqs = sorted(hist.values())

print('Part 1 answer: %d' % (freqs[-1] - freqs[0]))

for step in range(10, 40):
	polymer = polymerise(polymer, rules)

hist = makehist(polymer)
freqs = sorted(hist.values())

print('Part 2 answer: %d' % (freqs[-1] - freqs[0]))
