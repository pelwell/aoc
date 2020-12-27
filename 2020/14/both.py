#!/usr/bin/python

import string
import sys
import re

def masked_inc(val, mask):
	incval = (val | ~mask) + 1
	return (val & ~mask) | (incval & mask)

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

mask = re.compile(r"^mask = ([01X]{36})")
mem = re.compile(r"^mem\[(\d+)\] = (\d+)")

memory = {}
memory2 = {}
mask_set = 0
mask_clr = 0
mask_float = 0
float_cnt = 0

for line in fh:
	m = mask.match(line)
	if m:
		mask_val = m.group(1)
		mask_set = 0
		mask_clr = 0
		mask_float = 0
		float_cnt = 0
		for i in range(36):
			if mask_val[i] == '1':
				mask_set |= (1 << (35 - i))
			elif mask_val[i] == '0':
				mask_clr |= (1 << (35 - i))
			else:
				mask_float |= (1 << (35 - i))
				float_cnt += 1
	m = mem.match(line)
	if m:
		addr = int(m.group(1))
		value = int(m.group(2))
		memory[addr] = (value & ~mask_clr) | mask_set
		addr2 = (addr | mask_set) & ~mask_float
		for n in range(1 << float_cnt):
			memory2[addr2] = value
			addr2 = masked_inc(addr2, mask_float)

answer1 = sum(memory.values())
answer2 = sum(memory2.values())

print("Part 1 answer: %d" % answer1)
print("Part 2 answer: %d" % answer2)
