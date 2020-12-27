#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

field_re = re.compile(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$")
fh = open(infile, 'r');

fields = []

while True:
	line = fh.readline().rstrip()
	if line == "your ticket:":
		break
	m = field_re.match(line)
	if m != None:
		name = m.group(1)
		min1 = int(m.group(2))
		max1 = int(m.group(3))
		min2 = int(m.group(4))
		max2 = int(m.group(5))
		fields.append((name, min1, max1, min2, max2))

my_ticket = [int(i) for i in fh.readline().rstrip().split(',')]

while True:
	line = fh.readline().rstrip()
	if line == "nearby tickets:":
		break

field_matches = [ range(len(my_ticket)) for i in range(len(fields)) ]

invalid_sum = 0
while True:
	line = fh.readline().rstrip()
	if line == "":
		break
	ticket = [int(i) for i in line.split(',')]
	# i is the field number with the value being compared
	valid2 = True
	for i, value in enumerate(ticket):
		valid = False
		for j, field in enumerate(fields):
			if (value >= field[1] and value <= field[2]) or (value >= field[3] and value <= field[4]):
				valid = True
		if not valid:
			invalid_sum += value
			valid2 = False

	if valid2:
		for i, value in enumerate(ticket):
			for j, field in enumerate(fields):
				if not ((value >= field[1] and value <= field[2]) or (value >= field[3] and value <= field[4])):
					if i in field_matches[j]:
						field_matches[j].remove(i)
product = 1

matched = []
for matches in range(1, len(field_matches)+1):
	for j, m in enumerate(field_matches):
		if len(m) == matches:
			for f in m:
				if not f in matched:
					matched.append(f)
					if fields[j][0].startswith('departure'):
						product *= my_ticket[f]
					next

print("Part 1 answer: %d" % invalid_sum)
print("Part 2 answer: %d" % product)
