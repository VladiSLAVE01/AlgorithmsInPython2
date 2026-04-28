from itertools import count

n = int(input()) # количество видов бактерий
lst = []
for i in range(n):
	a = input().split()
	first = int(a[0])
	second = int(a[1])
	lst.append([first , second])
planet = list(map(int, input().split()))

result = []
for i in planet:
	count = 0
	for first, second in lst:
		if first <= i <= second:
			count += 1
	print(count)


