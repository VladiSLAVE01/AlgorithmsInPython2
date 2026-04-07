
arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

# Подсчитываем частоту каждого числа во втором массиве
freq = {}
for num in arr2:
    freq[num] = freq.get(num, 0) + 1

# Формируем ответ для каждого элемента первого массива
result = []
for num in arr1:
    result.append(freq.get(num, 0))

# Выводим результат
print(' '.join(map(str, result)))
