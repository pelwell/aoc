#!/usr/bin/python

import sys;

def count_bits(num):
	count = 0

	i = 1
	while num != 0:
		if (num & i) != 0:
			num &= ~i
			count += 1
		i <<= 1
	return count

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

linenum = 0
present_bits1 = 0
present_num1 = 0
count1 = 0
present_bits2 = ~0
count2 = 0

for line in fh:
	linenum += 1
	line = line.rstrip()
	if len(line) == 0:
		count1 += present_num1
		count2 += count_bits(present_bits2)
		present_num1 = 0
		present_bits1 = 0
		present_bits2 = ~0
	else:
		user_bits = 0

		for char in line:
			if char >= 'a' and char <= 'z':
				bit = (1 << (ord(char) - ord('a')))
				if (present_bits1 & bit) == 0:
					present_bits1 |= bit
					present_num1 += 1
				user_bits |= bit

		present_bits2 &= user_bits

count1 += present_num1
count2 += count_bits(present_bits2)

print("Part 1 answer: %d" % count1)
print("Part 2 answer: %d" % count2)
