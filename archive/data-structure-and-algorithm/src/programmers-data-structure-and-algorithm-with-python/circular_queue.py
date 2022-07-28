class CircularQueue:
    def __init__(self, n):
        self.max_count = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.max_count

    def enqueue(self, x):
        if self.is_full():
            raise IndexError('Queue is full!')

        self.rear = (self.rear + 1) % self.max_count
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        self.front = (self.front + 1) % self.max_count
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        return self.data[(self.front + 1) % self.max_count]
