def choice_sort(arr):
    n = len(arr)
    half = n // 2
    count = 0

    if half == 0:
        print(*arr)

    len_arr = n
    a = arr  # локальная ссылка на список ускоряет доступ

    for i in range(len_arr):
        min_i = i
        ai = a[i]

        for j in range(i + 1, len_arr):
            if a[j] < a[min_i]:
                min_i = j

        # swap
        a[i], a[min_i] = a[min_i], a[i]
        count += 1

        if count == half:
            print(*a)

    return a

# def choice_sort(arr):
# 	n = len(arr)
# 	half = n // 2
# 	count = 0
#
# 	if half == 0:
# 		print(*arr)
#
# 	for num in range(len(arr)):
# 		min_val = num
#
# 		for item in range(num, len(arr)):
# 			if arr[min_val] > arr[item]:
# 				min_val = item
#
# 		arr[num], arr[min_val] = arr[min_val], arr[num]
# 		count += 1
#
# 		if count == half:
# 			print(*arr)
# 	return arr

arr = list(map(int, input().split()))

result = choice_sort(arr)
print(' '.join(map(str, result)))