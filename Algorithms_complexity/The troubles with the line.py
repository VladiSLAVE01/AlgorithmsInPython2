lst = list(map(int, input().split()))


def sort(lst):
	if len(lst) < 2:
		return lst
	l = []
	r = []
	pivot2 = lst[-1]

	# Разбиение с сохранением порядка
	for i in lst[:-1]:
		if i < pivot2:
			l.append(i)
		if i >= pivot2:
			r.append(i)

	# Разворачиваем l, чтобы последний элемент был максимальным (как в примере)
	l = l[::-1]

	# Выводим pivot ТОЛЬКО если есть что разбивать (оба подмассива не пустые)
	# Но в примере выводят даже если один пустой, поэтому выводим всегда
	print(pivot2)

	l = sort(l)
	r = sort(r)
	return l + [pivot2] + r


print(*sort(lst))

# def quicksort(arr, left, right, result):
# 	"""Рекурсивная быстрая сортировка с выводом последних элементов групп"""
# 	if left >= right:
# 		return
#
# 	# Выводим последний элемент текущей группы (опорный)
# 	result.append(str(arr[right]))
#
# 	# Разбиение: опорный элемент — последний
# 	pivot = arr[right]
# 	i = left - 1
#
# 	for j in range(left, right):
# 		if arr[j] <= pivot:
# 			i += 1
# 			arr[i], arr[j] = arr[j], arr[i]
#
# 	# Ставим опорный элемент на правильное место
# 	arr[i + 1], arr[right] = arr[right], arr[i + 1]
# 	pivot_index = i + 1
#
# 	# Рекурсивно сортируем левую и правую части
# 	quicksort(arr, left, pivot_index - 1, result)
# 	quicksort(arr, pivot_index + 1, right, result)
#
#
# # Ввод данных
# lst = list(map(int, input().split()))
#
# # Список для хранения выводимых опорных элементов
# output = []
#
# # Запускаем быструю сортировку
# quicksort(lst, 0, len(lst) - 1, output)
#
# # Выводим опорные элементы (каждый на новой строке)
# print("\n".join(output))
#
# # Выводим отсортированный массив
# print(" ".join(map(str, lst)))