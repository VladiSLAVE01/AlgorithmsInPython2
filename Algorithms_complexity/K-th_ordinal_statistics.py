lst = list(map(int, input().split()))
k = int(input())
def k_th(lst, k):
	pivot = lst[-1]
	if len(lst) == 1:
		return lst[0]

	l = []
	r = []
	m = []
	for i in lst:
		if i < pivot:
			l.append(i)
		elif i > pivot:
			r.append(i)
		else:
			m.append(i)

	l_count = len(l)
	m_count = len(m)

	if k < l_count:
		return k_th(l, k)
	if k < l_count + m_count:
		return pivot
	else:
		return k_th(r, k - l_count - m_count)

print(k_th(lst, k))