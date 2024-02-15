class ListADT:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            self._resize_array()
        self.array[self.size] = value
        self.size += 1

    def _resize_array(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")


    def set(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def remove(self, value):
        index = self.index_of(value)
        if index != -1:
            self.remove_at(index)

    def remove_at(self, index):
        if 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError("Index out of range")

    def index_of(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def display(self):
        result = "["
        for i in range(self.size):
            result += str(self.array[i])
            if i < self.size - 1:
                result += ", "
        result += "]"
        return result

# Create a ListADT object
my_list = ListADT()

while True:
    print("\nMenu:")
    print("1. Append value")
    print("2. Set value at index")
    print("3. Remove value")
    print("4. Display list")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        value = input("Enter the value to append: ")
        my_list.append(value)
    elif choice == '2':
        index = int(input("Enter the index to set: "))
        value = input("Enter the new value: ")
        my_list.set(index, value)
    elif choice == '3':
        value = input("Enter the value to remove: ")
        my_list.remove(value)
    elif choice == '4':
        print("List:", my_list.display())
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
