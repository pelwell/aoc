#!/usr/bin/python

import re
import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

count1 = 0
count2 = 0

r = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)")

for line in fh:
	m = r.match(line)
	if m != None:
		a = int(m.group(1))
		b = int(m.group(2))
		letter = m.group(3)
		password = m.group(4)
		num = password.count(letter)
		if num >= a and num <= b:
			count1 += 1 
		c = password[a - 1]
		d = password[b - 1]
		if (c == letter) != (d == letter):
			count2 += 1

print("Part 1 answer: %d" % count1)
print("Part 2 answer: %d" % count2)
