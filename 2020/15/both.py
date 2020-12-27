#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

line = fh.readline().rstrip()

starters = [int(i) for i in line.split(',')]

last_seen = {}
last = 0
turn = 0

for num in starters:
	last_seen[last] = turn
	turn += 1
	last = num
	print("Turn %d: %d" % (turn, last))

print_at = 1000
while turn < 30000000:
	next = 0
	when = last_seen.get(last, 0)
	if when:
		next = turn - when
	last_seen[last] = turn
	turn += 1
	last = next
	if turn == 2020:
		print("Part 1 answer: %d" % last)
	if turn == print_at:
		print("%d: %d" % (turn, last))
		print_at *= 2

print("Part 2 answer: %d" % last)
