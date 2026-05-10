class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def add(self, val):
		if val < self.val:
			if self.left is None:
				self.left = TreeNode(val)
			else:
				self.left.add(val)
		else:
			if self.right is None:
				self.right = TreeNode(val)
			else:
				self.right.add(val)
		return self

	def delete(self, val):
		if val < self.val:
			if self.left:
				self.left = self.left.delete(val)
		elif val > self.val:
			if self.right:
				self.right = self.right.delete(val)
		else:
			if self.left is None:
				return self.right

			if self.right is None:
				return self.left

			parent = self
			min_node = self.right
			while min_node.left:
				parent = min_node
				min_node = min_node.left

			self.val = min_node.val

			if parent == self:
				self.right = min_node.right
			else:
				parent.left = min_node.right
		return self

	def find(self, val):
		if val == self.val:
			return self
		elif val < self.val:
			if self.left is None:
				return False
			return self.left.find(val)
		else:
			if self.right is None:
				return False
			return self.right.find(val)

	def next(self,val):
		current = self
		candidate = None

		while current:
			if val < current.val:
				candidate = current.val
				current = current.left
			elif val > current.val:
				current = current.right
			else:
				if current.right:
					temp = current.right
					while temp.left:
						temp = temp.left
					return temp.val
				return candidate
		return candidate

	def print_tree(self):
		if not self:
			return

		print(self.val)

		def dfs(node, prefix, is_last):
			if not node:
				return

			print(prefix + ('└───' if is_last else '├───') + str(node.val))

			# Проверяем наличие детей
			if node.left or node.right:
				new_prefix = prefix + ('    ' if is_last else '│   ')

				# Левый ребёнок (если есть)
				if node.left:
					# Левый ребёнок является последним, если нет правого ребёнка
					dfs(node.left, new_prefix, node.right is None)

				# Правый ребёнок (если есть) — всегда последний
				if node.right:
					dfs(node.right, new_prefix, True)

		# Обрабатываем детей корня
		if self.left:
			dfs(self.left, "", self.right is None)
		if self.right:
			dfs(self.right, "", True)


def main():
	# Сначала читаем первую строку — отсортированный массив
	first_line = input().strip()
	arr = list(map(int, first_line.split()))

	# Строим дерево из отсортированного массива (как в прошлой задаче)
	def build_tree(arr):
		if not arr:
			return None
		if len(arr) % 2 == 0:
			mid = len(arr) // 2 - 1
		else:
			mid = len(arr) // 2
		root = TreeNode(arr[mid])
		root.left = build_tree(arr[:mid])
		root.right = build_tree(arr[mid + 1:])
		return root

	root = build_tree(arr)

	# Обрабатываем команды
	while True:
		try:
			line = input().strip()
		except EOFError:
			break

		if not line:
			continue

		parts = line.split()
		cmd = parts[0]

		if cmd == 'exit':
			break

		elif cmd == 'add':
			# Добавляем все числа из команды (первое число после add)
			for i in range(1, len(parts)):
				root.add(int(parts[i]))
			print('Ok')

		elif cmd == 'delete':
			num = int(parts[1])
			root = root.delete(num)
			print('Ok')

		elif cmd == 'find':
			num = int(parts[1])
			result = root.find(num)
			if result and result.val == num:
				print("Число нашлось")
			else:
				print("Число не нашлось")

		elif cmd == 'next':
			num = int(parts[1])
			result = root.next(num)
			if result is None:
				print("Следующего числа нет")
			else:
				print(result)

		elif cmd == 'print':
			root.print_tree()

if __name__ == '__main__':
	main()
