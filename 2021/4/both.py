#!/usr/bin/python

import string
import sys
import re

COLS = 5
ROWS = 5

def cardsum(card):
	sum = 0
	idx = 0
	for num in card[0]:
		if num != None:
			sum += idx
		idx += 1
	return sum

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

firstline = True

cards = []

# Cards are:
#   sparse arrays of positions where the index appears on the card
#   array of counts of matches per row
#   array of counts of matches per column

rowidx = 0

for line in fh:
	line = line.rstrip()
	if line == "":
		continue
	if firstline:
		calls = [int(i) for i in line.split(',')]
		firstline = False
	else:
		if rowidx == 0:
			nums = [ None ] * (max(calls) + 1)
			card = [nums, [0] * ROWS, [0] * COLS, 0]
			cards.append(card)
		row = [int(i) for i in line.split()]
		for colidx in range(COLS):
			nums[row[colidx]] = rowidx * COLS + colidx
		rowidx = (rowidx + 1) % ROWS

winner_score = None
last_score = None

for call in calls:
	for card in cards:
		if card[3]:
			continue
		pos = card[0][call]
		if pos != None:
			card[0][call] = None
			card[1][int(pos/COLS)] += 1
			if card[1][pos / COLS] == ROWS:
				last_score = call * cardsum(card)
				if not winner_score:
					winner_score = last_score
				card[3] = 1

			card[2][pos%COLS] += 1
			if card[2][pos % COLS] == COLS:
				last_score = call * cardsum(card)
				if not winner_score:
					winner_score = last_score
				card[3] = 1

if not winner_score:
	print("Error - no winner found!")

print("Part 1 answer: %d" % (winner_score))
print("Part 2 answer: %d" % (last_score))
