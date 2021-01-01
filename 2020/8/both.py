#!/usr/bin/python

import sys;
import re;

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

def run_prog(prog, trace = False):
	acc = 0
	pos = 0
	visited = [False] * len(prog)

	while pos < len(prog) and not visited[pos]:
		instr = prog[pos]
		if trace:
			print("%d: %s %s // acc %d`" % (pos, instr[0], pos + instr[1], acc))
		visited[pos] = True
		if instr[0] == 'jmp':
			pos += instr[1]
		elif instr[0] == 'acc':
			acc += instr[1]
			pos += 1
		elif instr[0] == 'nop':
			pos += 1
		else:
			raise Exception("bad instruction at %d" % pos)
	return (pos, acc)
	
prog = []

instr_re = re.compile(r'(jmp|acc|nop) ([-+]\d+)')
for line in fh:
	m = instr_re.match(line)
	if m:
		prog.append((m.group(1), int(m.group(2))))

res = run_prog(prog)

print("Part 1 answer: %d" % res[1])

def switch(prog, pos):
	instr = prog[pos]
	if instr[0] == 'jmp':
		prog[pos] = ('nop', instr[1]) 
	elif instr[0] == 'nop':
		prog[pos] = ('jmp', instr[1]) 

for pos in range(len(prog)):
	switch(prog, pos)
	res = run_prog(prog)
	if res[0] == len(prog):
		break
	switch(prog, pos)

print("Part 2 answer: %d" % res[1])
