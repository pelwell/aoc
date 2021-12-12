#!/usr/bin/python

import string
import sys

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

for line in fh:
	vals = [int(i) for i in line.rstrip().split(',')]

vals.sort()

minpos = vals[len(vals)/2]

sad = 0
for v in vals:
        sad += abs(v - minpos)

print("Part 1 answer: %d" % (sad))

ssqus = []

for i in range(vals[0], vals[-1] + 1):
    ssqu = 0
    for v in vals:
        d = abs(v - i)
        ssqu += (d*(d+1))/2
    ssqus.append(ssqu)

print("Part 2 answer: %d" % (min(ssqus)))
