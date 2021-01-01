#!/usr/bin/python

import sys;
import re;

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

count1 = 0
count2 = 0
contains = {}
fitsin = {}

simple_re = re.compile(r'(?: bags?| contain| no other bags|[\.,\n])')
for line in fh:
	toks = simple_re.sub('', line).split()
	src = toks[0] + ' ' + toks[1]
	if not contains.has_key(src):
		contains[src] = []
	node = contains[src]
	for i in range(2, len(toks), 3):
		tp = toks[i+1] + ' ' + toks[i+2]
		node.append([ int(toks[i]), tp ])
		if not fitsin.has_key(tp):
			fitsin[tp] = []
		fitsin[tp].append(src)

containers = set([])

frontier = [ 'shiny gold' ]

while frontier:
	head = frontier[0]
	del frontier[0]

	if fitsin.has_key(head):
		for new in fitsin[head]:
			if not new in containers:
				containers.add(new)
				frontier.append(new)
				count1 += 1
	
print("Part 1 answer: %d" % count1)

frontier = [ (1, 'shiny gold') ]

while frontier:
	head = frontier[0]
	del frontier[0]
	mult = head[0]
	type = head[1]

	if contains.has_key(type):
		for node in contains[type]:
			new_count = mult * node[0]
			count2 += new_count
			frontier.append((new_count, node[1]))

print("Part 2 answer: %d" % count2)
