def rec(selected, m, n, k, results):
	if k == 0:
		results.append(' '.join(map(str, selected)))
		return

	if selected:
		upper = selected[-1] - 1
	else:
		upper = n

	lower = m + k - 1

	for num in range(upper, lower - 1, -1):
		rec(selected + [num], m, n, k - 1, results)


# Ввод
data = input().split()
k, m, n = int(data[0]), int(data[1]), int(data[2])

results = []
rec([], m, n, k, results)

# Вывод
for seq in results[::-1]:
	print(seq)
print(len(results))