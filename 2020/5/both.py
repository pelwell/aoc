#!/usr/bin/python

import sys

def get_seat_id(label):
	id = 0
	for char in label:
		if char == 'B' or char == 'R':
			id = (id << 1) | 1
		elif char == 'F' or char == 'L':
			id = (id << 1) | 0
	return id

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

linenum = 0
max_id = 0
seats = []

for line in fh:
	linenum += 1
	id = get_seat_id(line)
	max_id = max(id, max_id)
	seats.append(id)

last_id = None
missing = None

print(seats)
seats.sort()

for id in seats:
	if last_id != None:
		if id != (last_id + 1):
			missing = last_id + 1	
			break
	last_id = id

print("Part 1 answer: %d" % max_id)
print("Part 2 answer: %d" % missing)
