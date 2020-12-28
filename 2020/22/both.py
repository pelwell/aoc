#!/usr/bin/python

import string
import sys
import re

player_1 = 0
player_2 = 1

def round(hands):
	if hands[0][0] > hands[1][0]:
		winner = player_1
		loser = player_2
	else:
		winner = player_2
		loser = player_1
	hands[winner] = hands[winner][1:] + hands[winner][0:1] + hands[loser][0:1]
	hands[loser] = hands[loser][1:]
	return winner

def list_to_str(l):
	return ",".join([str(x) for x in l])

def rec_game(hands):
	seen = {}
	rounds = 0
	winner = 0
	while True:
		sig = list_to_str(hands[0]) + "|" + list_to_str(hands[1])
		if seen.has_key(sig):
			return 0
		seen[sig] = 1
		winner = rec_round(hands)
		rounds += 1
		if len(hands[1 - winner]) == 0:
			break
	return winner

def rec_round(hands):
	top_0 = hands[0][0]
	top_1 = hands[1][0]
	if top_0 < len(hands[0]) and top_1 < len(hands[1]):
		winner = rec_game([hands[0][1:top_0+1], hands[1][1:top_1+1]])
	elif top_0 > top_1:
		winner = player_1
	else:
		winner = player_2
	loser = 1 - winner
	hands[winner] = hands[winner][1:] + hands[winner][0:1] + hands[loser][0:1]
	hands[loser] = hands[loser][1:]
	return winner

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

fh = open(infile, 'r');

player_re = re.compile(r"Player (\d):")

hands = []
plyr = 0
hand = None
for line in fh:
	line = line.rstrip()
	if line == "":
		continue
	m = player_re.match(line)
	if m:
		plyr = int(m.group(1))
		hand = []
		hands.append(hand)
	else:
		hand.append(int(line))

hands2 = [ hands[0][:], hands[1][:] ]

winner = None
rounds = 0
while True:
	win = round(hands)
	rounds += 1
	if len(hands[1 - win]) == 0:
		winner = hands[win]
		break

part1 = 0
for i in range(len(winner)):
	part1 += winner[i] * (len(winner) - i)

print("Part 1 answer: %s" % part1)

winner = hands2[rec_game(hands2)]

part2 = 0
for i in range(len(winner)):
	part2 += winner[i] * (len(winner) - i)

print("Part 2 answer: %d" % part2)
