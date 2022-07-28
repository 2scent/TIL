from array_queue import ArrayQueue


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = [self.data]
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        return self.root.size() if self.root else 0

    def depth(self):
        return self.root.depth() if self.root else 0

    def inorder(self):
        return self.root.inorder() if self.root else []

    def preorder(self):
        return self.root.preorder() if self.root else []

    def postorder(self):
        return self.root.postorder() if self.root else []

    def bft(self):
        traversal = []
        q = ArrayQueue()

        if self.root:
            q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            traversal.append(node.data)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal
