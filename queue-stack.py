class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = []  # Stack for enqueue operations
        self.dequeue_stack = []  # Stack for dequeue operations

    def is_empty(self):
        return not (self.enqueue_stack or self.dequeue_stack)

    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None  # Queue is empty
            # Transfer elements from enqueue stack to dequeue stack to reverse the order
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front of the Queue:", queue.dequeue())  # 1
print("Dequeue:", queue.dequeue())            # 2

queue.enqueue(4)
print("Size of the Queue:", queue.size())     # 1
