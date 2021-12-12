#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

firstline = True

bitstrings = []

for line in fh:
	line = line.rstrip()
	bitstrings.append(line)
	if firstline:
		firstline = False
		bits = len(line)
		counts = [0] * bits
	for i in range(bits):
		if line[i] == '1':
			counts[i] += 1
		else:
			counts[i] -= 1
gamma = 0
for i in range(bits):
	if counts[i] > 0:
		gamma += (1 << (bits - i - 1))
epsilon = gamma ^ ((1 << bits) - 1)

print("Part 1 answer: %d" % (gamma * epsilon))

def bitsplit(set, pos):
	zeroes = []
	ones = []
	for bs in set:
		if bs[pos] == '0':
			zeroes.append(bs)
		else:
			ones.append(bs)
	if len(zeroes) > len(ones):
		return (zeroes, ones)
	else:
		return (ones, zeroes)

def bits_to_num(bs):
	num = 0
	for i in range(bits):
		num <<= 1
		if bs[i] == '1':
			num += 1
	return num

def oxygen(set):
	for i in range(bits):
		if len(set) == 1:
			break
		set = bitsplit(set, i)[0]
	return bits_to_num(set[0])

def co2(set):
	for i in range(bits):
		if len(set) == 1:
			break
		set = bitsplit(set, i)[1]
	return bits_to_num(set[0])

print("Part 2 answer: %d" % (oxygen(bitstrings) * co2(bitstrings)))
