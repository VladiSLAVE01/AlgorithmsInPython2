from sys import stdin
from collections import defaultdict


def solve():
	a = list(map(int, stdin.readline().split()))
	n = len(a)

	queries = list(map(int, stdin.readline().split()))

	positions = defaultdict(list)
	for i, height in enumerate(a):
		positions[height].append(i)

	cache = {}
	results = []

	for x in queries:
		if x in cache:
			results.append(cache[x])
			continue

		if x not in positions:
			cache[x] = 0
			results.append(0)
			continue

		pos_list = positions[x]
		total = len(pos_list)

		max_f = 0

		CL = 0
		CR = n - 0 - total + CL
		f = CL * CR
		if f > max_f:
			max_f = f

		for k, idx in enumerate(pos_list):
			p = idx + 1
			CL = k + 1
			CR = n - p - total + CL
			f = CL * CR
			if f > max_f:
				max_f = f

		CL = total
		CR = n - n - total + CL
		f = CL * CR
		if f > max_f:
			max_f = f

		cache[x] = max_f
		results.append(max_f)

	print(' '.join(map(str, results)))


if __name__ == "__main__":
	solve()