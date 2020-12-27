#!/usr/bin/python

import string
import sys
import re

def calc_loops(target):
	subject = 7
	value = 1
	loops = 0
	while value != target:
		value *= subject
		value %= modulus
		loops += 1
	return loops

def iterate(subject, loops):
	value = 1
	for i in range(loops):
		value *= subject
		value %= modulus
	return value

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

card_public = int(fh.readline().rstrip())
door_public = int(fh.readline().rstrip())

modulus = 20201227

card_loops = calc_loops(card_public)
key = iterate(door_public, card_loops)

print("Part 1 answer: %d" % key)
