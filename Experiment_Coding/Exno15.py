class Node:
    def __init__(self, value):
        self.data, self.left, self.right = value, None, None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search(root.left if key < root.data else root.right, key)
root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)
print("Inorder Traversal:")
inorder(root)
key = int(input("\nEnter register number to search: "))
print("Student Record Found" if search(root, key)
      else "Student Record Not Found")