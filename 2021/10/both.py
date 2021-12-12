#!/usr/bin/python

import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

delimiters = {
	'(':(1, 0), ')':(1, 3),
	'[':(2, 0), ']':(2, 57),
	'{':(3, 0), '}':(3, 1197),
	'<':(4, 0), '>':(4, 25137),
}

sum1 = 0
score2s = []

for line in fh:
	opens = []
	score1 = 0
	for d in line.rstrip():
		(t, s) = delimiters[d]
		if s == 0:
			opens.append(t)
		else:
			o = opens.pop()
			if t != o:
				score1 = s
				break
	if score1:
		sum1 += score1
	else:
		score2 = 0
		for d in opens[::-1]:
			score2 = 5 * score2 + d
		score2s.append(score2)

score2s.sort()

print("Part 1 answer: %d" % (sum1))
print("Part 2 answer: %d" % (score2s[len(score2s)/2]))
