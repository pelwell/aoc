#!/usr/bin/python

import string
import sys

def to_bits(seq):
	num = 0
	if seq != '|':
		for c in seq:
			num += (1 << (ord(c)-ord('a')))
	return num

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

count1 = 0
sum2 = 0

for line in fh:
	tokens = [ (len(s), to_bits(s)) for s in line.rstrip().split()]
	bits_to_digit = {}
	fives = []
	sixes = []
	for i in range(10):
		(l, bits) = tokens[i]
		if l == 2:
			bits_to_digit[bits] = '1'
			one = bits
		elif l == 3:
			bits_to_digit[bits] = '7'
		elif l == 4:
			bits_to_digit[bits] = '4'
			four = bits
		elif l == 5:
			fives.append(bits)
		elif l == 6:
			sixes.append(bits)
		elif l == 7:
			bits_to_digit[bits] = '8'
			eight = bits

	for s in sixes:
		if s & four == four:
			bits_to_digit[s] = '9'
			nine = s
		elif s & one == one:
			bits_to_digit[s] = '0'
			zero = s
		else:
			bits_to_digit[s] = '6'
			six = s

	five = six & nine
	for f in fives:
		if f == five:
			bits_to_digit[f] = '5'
		elif f & one == one:
			bits_to_digit[f] = '3'
		else:
			bits_to_digit[f] = '2'

	output = ''
	for i in range(11,15):
		digit = bits_to_digit.get(tokens[i][1], '?')
		output += digit
		if digit in '1478':
			count1 += 1

	sum2 += int(output)

print("Part 1 answer: %d" % (count1))
print("Part 2 answer: %d" % (sum2))
