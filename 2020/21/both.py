#!/usr/bin/python

import string
import sys
import re

infile = 'input.txt'
if (len(sys.argv) > 1):
	infile = sys.argv[1]

food_re = re.compile(r"^([a-z ]+) \(contains ([a-z ,]+)\)")

fh = open(infile, 'r');

# Allergens appear in exactly one ingredient, so are effectively translations.
# Allergens are not always labelled, but all foods show to containi an allergen
# must share a common ingredient

# Determine which ingredients cannot possibly contain any of the allergens in your
# list. How many times do any of those ingredients appear?

# An item cannot be a 

foods = []

allergens = {}
unresolved_allergens = {}

for line in fh:
	m = food_re.match(line)
	if m:
		alls = set(m.group(2).split(', '))
		fds = set(m.group(1).split())
		foods.append([fds, alls])
		for a in alls:
			if unresolved_allergens.has_key(a):
				unresolved_allergens[a].intersection_update(fds)
			else:
				unresolved_allergens[a] = fds.copy()

unresolved_allergens = unresolved_allergens.items()

while unresolved_allergens:
	a = unresolved_allergens[0]
	unresolved_allergens[:1] = []
	if len(a[1]) == 1:
		# This is resolved
		ingredient = list(a[1])[0]
		allergens[a[0]] = ingredient
		# remove it from the lists of other possibilities
		for b in unresolved_allergens:
			if ingredient in b[1]:
				b[1].remove(ingredient)
	else:
		unresolved_allergens.append(a)

part1 = 0

for f in foods:
	for i in f[0]:
		if not i in allergens.values():
			part1 += 1

print("Part 1 answer: %d" % part1)

part2 = allergens.keys()
part2.sort()
part2 = ",".join([allergens[x] for x in part2])

print("Part 2 answer: %s" % part2)
