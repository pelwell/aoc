#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

seq_re = re.compile(r'^(\d+): ([0-9 ]+)$')
alt_re = re.compile(r'^(\d+): ([0-9 ]+) \| ([0-9 ]+)$')
term_re = re.compile(r'^(\d+): "([a-z])"$')

def matches(rules, rule, message, pos, depth):
	#print("%smatches(%d, %s, %d)" % ("  " * depth, rule, message, pos))
	r = rules[rule]
	mends = []
	if pos < len(message):
		if r[0] == 't':
			if message[pos] == r[1]:
				mends.append(pos + 1)
		elif r[0] == 's':
			ends = []
			p1 = [ pos ]
			for r2 in r[1]:
				p2 = []
				for p in p1:
					p2.extend(matches(rules, r2, message, p, depth + 1))
				p1 = p2
				ends = p1
			mends.extend(ends)

		elif r[0] == 'a':
			ends = []
			p1 = [ pos ]
			for r2 in r[1]:
				p2 = []
				for p in p1:
					p2.extend(matches(rules, r2, message, p, depth + 1))
				p1 = p2
				ends = p1
			mends.extend(ends)
			ends = []
			p1 = [ pos ]
			for r2 in r[2]:
				p2 = []
				for p in p1:
					p2.extend(matches(rules, r2, message, p, depth + 1))
				p1 = p2
				ends = p1
			mends.extend(ends)
	#print("%smatches(%d, %s, %d) -> " % ("  " * depth, rule, message, pos), mends)
	return mends

rules = {}

while True:
	line = fh.readline().rstrip()
	if len(line) == 0:
		break
	m1 = seq_re.match(line)
	m2 = alt_re.match(line)
	m3 = term_re.match(line)
	if m1:
		rule = int(m1.group(1))
		a = [ int(x) for x in m1.group(2).split(' ') ]
		rules[rule] = ('s', a)
	elif m2:
		rule = int(m2.group(1))
		a = [ int(x) for x in m2.group(2).split(' ') ]
		b = [ int(x) for x in m2.group(3).split(' ') ]
		rules[rule] = ('a', a, b)
	elif m3:
		rule = int(m3.group(1))
		rules[rule] = ('t', m3.group(2))

rules2 = rules.copy()
rules2[8] = ( 'a', [ 42 ], [ 42, 8 ])
rules2[11] = ( 'a', [ 42, 31 ], [ 42, 11, 31 ])

count = 0
count2 = 0

while True:
	message = fh.readline().rstrip()
	if len(message) == 0:
		break
	for m in matches(rules, 0, message, 0, 0):
		if m == len(message):
			count += 1
			break
	for m in matches(rules2, 0, message, 0, 0):
		if m == len(message):
			count2 += 1
			break

print("Part 1 answer: %d" % count)
print("Part 2 answer: %d" % count2)
