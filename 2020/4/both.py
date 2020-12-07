#!/usr/bin/python

import re
import string
import sys

def is_byr(x):
	if (x.isdigit()):
		x = int(x)
		if (x >= 1920) and (x <= 2002):
			return True
	return False

def is_iyr(x):
	if (x.isdigit()):
		x = int(x)
		if (x >= 2010) and (x <= 2020):
			return True
	return False

def is_eyr(x):
	if (x.isdigit()):
		x = int(x)
		if (x >= 2020) and (x <= 2030):
			return True
	return False

def is_hgt(x):
	if len(x) < 4:
		return False
	num = x[:-2]
	if num.isdigit():
		num = int(num)
		units = x[-2:]
		if units == 'cm':
			return ((num >= 150) and (num <= 193))
		if units == 'in':
			return ((num >= 59) and (num <= 76))
	return False

def is_hcl(x):
	if len(x) == 7 and x[0] == '#':
		return all(c in string.hexdigits for c in x[1:])
	return False

def is_ecl(x):
	return x in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }

def is_pid(x):
	return len(x) == 9 and x.isdigit()

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

fields = {
	'byr': (0x01, is_byr),
	'iyr': (0x02, is_iyr),
	'eyr': (0x04, is_eyr),
	'hgt': (0x08, is_hgt),
	'hcl': (0x10, is_hcl),
	'ecl': (0x20, is_ecl),
	'pid': (0x40, is_pid),
}

valid1 = 0
present1 = 0
valid2 = 0
present2 = 0
linenum = 0

r = re.compile(r"\b([a-z]{3}):([^ ]+)")

for line in fh:
	linenum += 1

	line = line.rstrip()
	if len(line) == 0:
		if present1 == 0x7f:
			valid1 += 1
		if present2 == 0x7f:
			valid2 += 1
		present1 = 0
		present2 = 0

	for m in r.finditer(line):
		if m.group(1) in fields:
			res = fields[m.group(1)]
			present1 |= res[0]
			if res[1](m.group(2)):
				present2 |= res[0]

if present1 == 0x7f:
	valid1 += 1
if present2 == 0x7f:
	valid2 += 1

print("Part 1 answer: %d" % valid1)
print("Part 2 answer: %d" % valid2)
