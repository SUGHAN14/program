class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
my_linked_list = LinkedList()

# Append some elements
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Prepend an element
my_linked_list.prepend(0)

# Display the linked list
print("Linked List:")
my_linked_list.display()

# Delete an element
my_linked_list.delete(2)

# Display the linked list after deletion
print("Linked List after deleting 2:")
my_linked_list.display()
