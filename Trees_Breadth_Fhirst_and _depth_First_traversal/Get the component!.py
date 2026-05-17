
n, v = map(int, input().split())

graph = []

for i in range(n):
	line = input().strip()

	if line == "-1":
		graph.append([])
	else:
		graph.append(list(map(int, line.split())))

visited = [False] * n
queue = [v]
visited[v] = True

while queue:
	cur = queue.pop(0)
	for neighbor in graph[cur]:
		if not visited[neighbor]:
			visited[neighbor] = True
			queue.append(neighbor)
result = [i for i in range(n) if visited[i]]
result.sort()
print(' '.join(map(str, result)))
