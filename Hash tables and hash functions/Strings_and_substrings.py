def prefix_function(s):
	n = len(s)
	pi = [0] * n

	for i in range(1, n):
		j = pi[i - 1]
		while j > 0 and s[i] != s[j]:
			j = pi[j - 1]
		if s[i] == s[j]:
			j += 1
		pi[i] = j

	return pi


def solve():
	s = input().strip()
	n = len(s)

	if n == 1:
		print(1, s)
		return

	pi = prefix_function(s)

	# Длина минимального повторяющегося паттерна
	pattern_len = n - pi[-1]

	# Проверяем, состоит ли строка из повторений
	if n % pattern_len == 0:
		k = n // pattern_len
		t = s[:pattern_len]
	else:
		k = 1
		t = s

	print(k, t)


if __name__ == "__main__":
	solve()
