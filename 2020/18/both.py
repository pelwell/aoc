#!/usr/bin/python

import string
import sys

def get_token(stream):
	while True:
		if stream[0] == len(stream[1]):
			return None
		c = stream[1][stream[0]]
		stream[0] += 1
		if c != ' ':
			return c

def next_token(stream):
	pos = stream[0]
	while True:
		if pos == len(stream[1]):
			return None
		c = stream[1][pos]
		pos += 1
		if c != ' ':
			return c

def get_term(stream):
	tok = get_token(stream)
	if tok.isdigit():
		return int(tok)
	elif tok == '(':
		return eval(stream)

def eval(stream):
	lhs = get_term(stream)
	while True:
		op = get_token(stream)
		if op == None:
			break
		if op == ')':
			break
		rhs = get_term(stream)
		if op == '+':
			lhs += rhs
		elif op == '*':
			lhs *= rhs
	return lhs

def get_term2(stream):
	tok = get_token(stream)
	if tok.isdigit():
		val = int(tok)
	elif tok == '(':
		val = eval2(stream)
	if next_token(stream) == '+':
		get_token(stream)
		val += get_term2(stream)
	return val

def eval2(stream):
	inpos = stream[0]
	lhs = get_term2(stream)
	while True:
		op = get_token(stream)
		if op == None:
			break
		if op == ')':
			break
		rhs = get_term2(stream)
		if op == '+':
			lhs += rhs
		elif op == '*':
			lhs *= rhs
	return lhs

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

sum = 0
sum2 = 0

for line in fh:
	stream = [ 0, line.rstrip()]
	value = eval(stream)
	sum += value
	stream[0] = 0

	value = eval2(stream)
	print(value)
	sum2 += value

print("Part 1 answer: %d" % sum)
print("Part 2 answer: %d" % sum2)
