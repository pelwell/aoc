from __future__ import print_function, division
import collections
import itertools
import fileinput
import heapq

grid = [s.rstrip() for s in fileinput.input()]

lingrid = list(itertools.chain.from_iterable(grid))
w, h = len(grid[0]), len(grid)
n = lingrid.index('@')
x, y = n % w, n // w
allkeys = set(c for c in lingrid if c.islower())

#grid[y-1] = grid[y-1][:x]   +  '#'  + grid[y-1][x+1:]
#grid[  y] = grid[y  ][:x-1] + '###' + grid[y  ][x+2:]
#grid[y+1] = grid[y+1][:x]   +  '#'  + grid[y+1][x+1:]
#
#pos = (
#  (x-1, y-1),
#  (x+1, y-1),
#  (x-1, y+1),
#  (x+1, y+1),
#)

pos = (
  (x, y),
)

def reachable_keys(sx, sy, keys):
    q = collections.deque([(sx, sy, 0)])
    seen = set()
    d = ( (-1, 0), (1, 0), (0, -1), (0, 1) )
    while q:
        cx, cy, l = q.popleft()
        if grid[cy][cx].islower() and grid[cy][cx] not in keys:
            yield l, cx, cy, grid[cy][cx]
            continue
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if ((nx, ny)) in seen:
                continue
            seen.add((nx, ny))

            c = grid[ny][nx]
            if c != '#' and (not c.isupper() or c.lower() in keys):
                q.append((nx, ny, l + 1))

q = [(0, pos, frozenset())]
seen = [set(), set(), set(), set()]
while q:
    d, cpos, keys = heapq.heappop(q)
    if keys == allkeys:
        print(d)
        break

    for i, (cx, cy) in enumerate(cpos):
        if (cx, cy, keys) in seen[i]:
            continue
        seen[i].add((cx, cy, keys))
        for l, nx, ny, key in reachable_keys(cx, cy, keys):
            npos = cpos[0:i] + ((nx, ny),) + cpos[i+1:]
            heapq.heappush(q, (d + l, npos, keys | frozenset([key])))
