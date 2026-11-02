
class BST:

    def __init__(self):
        self.tree = [None] * 100

    def insert(self, data):
        i = 0

        while i < 100:
            if self.tree[i] is None:
                self.tree[i] = data
                print("Element inserted")
                return

            if data < self.tree[i]:
                i = 2 * i + 1
            elif data > self.tree[i]:
                i = 2 * i + 2
            else:
                print("Duplicate elements not allowed")
                return

        print("Tree is full")

    def search(self, data):
        i = 0

        while i < 100 and self.tree[i] is not None:
            if self.tree[i] == data:
                return True

            if data < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        return False

    def delete(self, data):
        if not self.search(data):
            print("Element not found")
            return

        values = []

        def collect(i):
            if i >= 100 or self.tree[i] is None:
                return

            collect(2 * i + 1)

            if self.tree[i] != data:
                values.append(self.tree[i])

            collect(2 * i + 2)

        collect(0)

        self.tree = [None] * 100

        for value in values:
            self.insert(value)

        print("Element deleted")

    def inorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return

        self.inorder(2 * i + 1)
        print(self.tree[i], end=" ")
        self.inorder(2 * i + 2)

    def preorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return

        print(self.tree[i], end=" ")
        self.preorder(2 * i + 1)
        self.preorder(2 * i + 2)

    def postorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return

        self.postorder(2 * i + 1)
        self.postorder(2 * i + 2)
        print(self.tree[i], end=" ")

    def minimum(self):
        if self.tree[0] is None:
            print("Tree is empty")
            return

        i = 0

        while 2 * i + 1 < 100 and self.tree[2 * i + 1] is not None:
            i = 2 * i + 1

        print("Minimum:", self.tree[i])

    def count(self, i):
        if i >= 100 or self.tree[i] is None:
            return 0

        return 1 + self.count(2 * i + 1) + self.count(2 * i + 2)

    def height(self, i):
        if i >= 100 or self.tree[i] is None:
            return 0

        left = self.height(2 * i + 1)
        right = self.height(2 * i + 2)

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
        bst.insert(data)

    elif choice == 2:
        data = int(input("Enter element to delete: "))
        bst.delete(data)

    elif choice == 3:
        data = int(input("Enter element to search: "))

        if bst.search(data):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder:")
        bst.inorder(0)
        print()

    elif choice == 5:
        print("Preorder:")
        bst.preorder(0)
        print()

    elif choice == 6:
        print("Postorder:")
        bst.postorder(0)
        print()

    elif choice == 7:
        bst.minimum()

    elif choice == 8:
        print("Total Nodes:", bst.count(0))

    elif choice == 9:
        print("Height:", bst.height(0))

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
