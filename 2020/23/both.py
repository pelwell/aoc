#!/usr/bin/python

import string
import sys
import re

def round(hand):
	cur = hand[0][0]
	p1 = hand[cur]
	p2 = hand[p1]
	p3 = hand[p2]
	hand[cur] = hand[p3]
	dest = ((cur - 2) % hand[0][1]) + 1
	while p1 == dest or p2 == dest or p3 == dest:
		dest = ((dest - 2) % hand[0][1]) + 1
	hand[p3] = hand[dest]
	hand[dest] = p1
	hand[0][0] = hand[cur]

def check(hand):
	seen = [0] * (hand[0][1] + 1)
	for val in hand[1:]:
		if seen[val]:
			print("* %d repeated" % val)
		seen[val] += 1

def handstring(hand):
	s = ''
	start = hand[0][0]
	cur = start
	while True:
		s += str(cur)
		cur = hand[cur]
		if cur == start:
			break
	return s

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

hand = [int(x) for x in list(fh.readline().rstrip())]
hand1 = range(10)
hand2 = range(1000001)
prev = hand[0]
for i in hand[1:]:
	hand1[prev] = hand1[i]
	prev = i
hand2[:11] = hand1

hand1[0] = [hand[0], 9]
hand2[0] = [hand[0], 1000000]
hand1[prev] = hand[0]
hand2[prev] = 10
hand2.append(hand[0])

for i in range(100):
	round(hand1)

hand1[0][0] = 1
labels = handstring(hand1)[1:]
print("Part 1 answer: %s" % labels)

for i in range(10000000):
	round(hand2)

part2 = hand2[1] * hand2[hand2[1]]
print("Part 2 answer: %d" % part2)
