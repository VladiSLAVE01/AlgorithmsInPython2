import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(arr):
    if not arr:
        return None
    n = len(arr)
    if n % 2 == 0:
        mid = n // 2 - 1
    else:
        mid = n // 2
    root = TreeNode(arr[mid])
    root.left = build_tree(arr[:mid])
    root.right = build_tree(arr[mid + 1:])
    return root


def print_tree(root):
    if not root:
        return

    def dfs(node, prefix, is_last):
        if not node:
            return

        print(prefix + ('└───' if is_last else '├───') + str(node.val))

        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            dfs(child, prefix + ('    ' if is_last else '│   '), is_last_child)

    print(root.val)
    children = []
    if root.left:
        children.append(root.left)
    if root.right:
        children.append(root.right)

    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        dfs(child, '', is_last)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    arr = list(map(int, data))
    root = build_tree(arr)
    print_tree(root)


if __name__ == "__main__":
    main()