class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class StackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a stack using linked list
my_stack = StackUsingLinkedList()

# Push some elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Display the stack
print("Stack:")
my_stack.display()

# Pop an element from the stack
popped_element = my_stack.pop()
print("Popped element:", popped_element)

# Peek at the top element of the stack
print("Peek:", my_stack.peek())

# Display the stack after popping
print("Stack after popping:")
my_stack.display()
