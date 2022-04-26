"""Модуль для создания Tree map."""

from itertools import chain


class TreeNode:
    """Модуль для создания узла дерева."""

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(key={self.key}, value={self.value}"

    def __eq__(self, other):
        if self.key == other.key and self.value == other.value:
            return True
        return False


class TreeMap:
    """Модуль для создания Tree map."""

    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        def inner_setitem(node):
            if node is None:
                return TreeNode(key, value)
            else:
                if key == node.key:
                    node.value = value
                elif key < node.key:
                    node.left = inner_setitem(node.left)
                else:
                    node.right = inner_setitem(node.right)
                return node
        self.root = inner_setitem(self.root)

    def __getitem__(self, key):
        def inner_getitem(node):
            if node is None:
                raise KeyError
            if key == node.key:
                return node.value
            elif key < node.key:
                return inner_getitem(node.left)
            else:
                return inner_getitem(node.right)
        return inner_getitem(self.root)

    @staticmethod
    def find_min_node(node):
        """Метод для нахождения самого левого узла без потомков(минимальный узел)."""

        if node.left is not None:
            return TreeMap.find_min_node(node.left)
        return node

    def __delitem__(self, key):
        def inner_delitem(node, key):
            if node is None:
                raise KeyError
            if key < node.key:
                node.left = inner_delitem(node.left, key)
                return node
            elif key > node.key:
                result = inner_delitem(node.right, key)
                node.right = result
                return node
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is not None and node.right is None:
                    return node.left
                elif node.left is None and node.right is not None:
                    return node.right
                else:
                    min_node = TreeMap.find_min_node(node.right)
                    node.key = min_node.key
                    node.value = min_node.value
                    node.right = inner_delitem(node.right, min_node.key)
                    return node
        self.root = inner_delitem(self.root, key)

    def __str__(self):
        nodes = [self.root]
        lines = []
        while any(nodes):
            lines.append('\t'.join(str(node and node.key) for node in nodes))
            nodes = list(chain.from_iterable([node and node.left, node and node.right] for node in nodes))
        return "\n".join(lines)

    def __iter__(self):
        def iter_node(node):
            if node is not None:
                yield from iter_node(node.left)
                yield node.key, node.value
                yield from iter_node(node.right)
        yield from iter_node(self.root)
