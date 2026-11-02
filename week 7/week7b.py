
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert operation
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            print("Duplicate elements not allowed")

        return root

    # Search operation
    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)

        return self.search(root.right, data)

    # Find minimum node
    def find_min(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    # Delete operation
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Minimum operation
    def minimum(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.find_min(self.root)
        print("Minimum:", temp.data)

    # Maximum operation
    def maximum(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.right is not None:
            temp = temp.right

        print("Maximum:", temp.data)

    # Count operation
    def count(self, root):
        if root is None:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)

    # Height operation
    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)


# Main Program

bst = BST()

while True:
    print("\n----- BST MENU -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Find Minimum")
    print("8. Count Nodes")
    print("9. Find Height")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        bst.root = bst.insert(bst.root, data)

    elif choice == 2:
        data = int(input("Enter element to delete: "))

        if bst.search(bst.root, data):
            bst.root = bst.delete(bst.root, data)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice == 3:
        data = int(input("Enter element to search: "))

        if bst.search(bst.root, data):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder:")
        bst.inorder(bst.root)
        print()

    elif choice == 5:
        print("Preorder:")
        bst.preorder(bst.root)
        print()

    elif choice == 6:
        print("Postorder:")
        bst.postorder(bst.root)
        print()

    elif choice == 7:
        bst.minimum()

    elif choice == 8:
        print("Total Nodes:", bst.count(bst.root))

    elif choice == 9:
        print("Height:", bst.height(bst.root))

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
