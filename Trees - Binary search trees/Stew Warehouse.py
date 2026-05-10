class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.count = 1  # количество банок с таким весом

	def add(self, val):
		"""Добавить банку массой val"""
		if val < self.val:
			if self.left is None:
				self.left = TreeNode(val)
			else:
				self.left.add(val)
		elif val > self.val:
			if self.right is None:
				self.right = TreeNode(val)
			else:
				self.right.add(val)
		else:  # val == self.val
			self.count += 1
		return self

	def delete(self, val):
		"""Удалить одну банку массой val"""
		if val < self.val:
			if self.left:
				self.left = self.left.delete(val)
		elif val > self.val:
			if self.right:
				self.right = self.right.delete(val)
		else:  # val == self.val
			if self.count > 1:
				self.count -= 1
				return self

			# Удаляем узел полностью
			if self.left is None:
				return self.right
			if self.right is None:
				return self.left

			# У узла два ребёнка
			parent = self
			min_node = self.right
			while min_node.left:
				parent = min_node
				min_node = min_node.left

			self.val = min_node.val
			self.count = min_node.count

			if parent == self:
				self.right = min_node.right
			else:
				parent.left = min_node.right
		return self

	def find(self, val):
		"""Найти банку массой val"""
		if val == self.val:
			return self
		elif val < self.val:
			if self.left is None:
				return None
			return self.left.find(val)
		else:
			if self.right is None:
				return None
			return self.right.find(val)

	def get_min(self):
		"""Найти минимальный вес"""
		current = self
		while current.left:
			current = current.left
		return current.val

	def get_max(self):
		"""Найти максимальный вес"""
		current = self
		while current.right:
			current = current.right
		return current.val

	def inorder_list(self, result):
		"""Обход дерева для list (с учётом count)"""
		if self.left:
			self.left.inorder_list(result)
		result.extend([self.val] * self.count)
		if self.right:
			self.right.inorder_list(result)


def build_balanced_tree(arr):
	"""Построение сбалансированного дерева из отсортированного массива"""
	if not arr:
		return None

	# Выбираем медиану для балансировки
	mid = (len(arr) - 1) // 2
	root = TreeNode(arr[mid])
	root.left = build_balanced_tree(arr[:mid])
	root.right = build_balanced_tree(arr[mid + 1:])
	return root


def main():
	# Читаем первую строку — отсортированный список весов
	first_line = input().strip()
	if first_line:
		initial_weights = list(map(int, first_line.split()))
	else:
		initial_weights = []

	# Строим сбалансированное дерево
	root = build_balanced_tree(initial_weights)

	# Обрабатываем команды
	while True:
		try:
			line = input().strip()
			if not line:
				continue

			parts = line.split()
			cmd = parts[0]

			if cmd == 'exit':
				break

			elif cmd == 'add':
				x = int(parts[1])
				if root is None:
					root = TreeNode(x)
				else:
					root.add(x)
				print("Ok")

			elif cmd == 'delete':
				x = int(parts[1])
				if root is not None:
					root = root.delete(x)
				print("Ok")

			elif cmd == 'find':
				x = int(parts[1])
				if root is None:
					print("Такой банки нет")
				else:
					node = root.find(x)
					if node and node.val == x:
						print("Такая банка есть")
					else:
						print("Такой банки нет")

			elif cmd == 'min':
				if root is None:
					print("Склад пуст")
				else:
					print(root.get_min())

			elif cmd == 'max':
				if root is None:
					print("Склад пуст")
				else:
					print(root.get_max())

			elif cmd == 'list':
				if root is None:
					print()
				else:
					result = []
					root.inorder_list(result)
					print(' '.join(map(str, result)))

		except EOFError:
			break


if __name__ == '__main__':
	main()