import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def postorder(self, node=None):
        if not node:
            node = self.root

        traversal = []
        if node.left:
            traversal += self.postorder(node.left)
        if node.right:
            traversal += self.postorder(node.right)
        traversal.append(node.data)
        return traversal

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        node = self.root
        while True:
            if node.data > data:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(data)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(data)
                    break


bst = BinarySearchTree()
while True:
    try:
        bst.insert(int(input()))
    except:
        break

print('\n'.join(map(str, bst.postorder())))
