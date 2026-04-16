def insertion_sort(lst):
	n = len(lst)
	half = (n -1 ) // 2

	if half == 0:
		print(*lst)

	for item in range(1, n):
		current_value = lst[item]
		position = item

		while position > 0 and current_value < lst[position - 1]:
			lst[position] = lst[position - 1]
			position -= 1

		lst[position] = current_value

		if item == half:
			print(*lst)
	return lst


lst = list(map(int, input().split()))
result = insertion_sort(lst)
print(*result)