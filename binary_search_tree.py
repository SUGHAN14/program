class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def in_order_traversal(self):
        self._in_order_traversal(self.root)
        print()

    def _in_order_traversal(self, root):
        if root:
            self._in_order_traversal(root.left)
            print(root.key, end=' ')
            self._in_order_traversal(root.right)

# Creating a binary search tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# In-order traversal to print the elements in ascending order
print("In-order traversal of the binary search tree:")
bst.in_order_traversal()

# Searching for a key
search_key = 40
result = bst.search(search_key)
if result:
    print(f"Key {search_key} found in the tree.")
else:
    print(f"Key {search_key} not found in the tree.")
