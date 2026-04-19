import sys


def merge_count(arr):
	if len(arr) <= 1:
		return arr, 0

	mid = len(arr) // 2
	left, inv_left = merge_count(arr[:mid])
	right, inv_right = merge_count(arr[mid:])

	merged = []
	i = j = 0
	inv = inv_left + inv_right

	# Слияние с подсчётом пар
	while i < len(left) and j < len(right):
		if left[i] >= right[j]:
			# Все оставшиеся в left подходят для right[j]
			inv += len(left) - i
			merged.append(right[j])
			j += 1
		else:
			merged.append(left[i])
			i += 1

	merged.extend(left[i:])
	merged.extend(right[j:])

	return merged, inv


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return

	n = int(data[0])
	arr = list(map(int, data[1:1 + n]))

	_, result = merge_count(arr)
	print(result)


if __name__ == '__main__':
	main()