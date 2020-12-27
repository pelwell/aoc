#!/usr/bin/python

import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

count2 = 0

line = fh.readline()
line = line.rstrip()
time = int(line)

line = fh.readline()
line = line.rstrip()

items = line.split(',')

min_wait = 1000
earliest_bus = None

for item in items:
	if item.isdigit():
		busid = int(item)
		wait = (-time) % busid
		if wait < min_wait:
			earliest_bus = busid
			min_wait = wait

print("Part 1 answer: %d" % (earliest_bus * min_wait))

time = 0
offset = 0
period = int(items.pop(0))

for item in items:
	offset += 1
	if item.isdigit():
		busid = int(item)
		while True:
			if ((time + offset) % busid) == 0:
				break
			time += period
		period *= busid

print("Part 2 answer: %d" % time)
