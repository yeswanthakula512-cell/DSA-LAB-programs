class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            self.insert_end_value(data)

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_end_value(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def insert_end(self):
        data = int(input("Enter data: "))
        self.insert_end_value(data)

    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                return

            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            return

        if self.head is None:
            print("Index out of range")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range")
                return

        new_node = Node(data)

        new_node.next = temp.next
        temp.next = new_node

    def delete_value(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        value = int(input("Enter value to delete: "))

        current = self.head
        previous = None

        while True:

            if current.data == value:

                if current == self.head:

                    if current.next == self.head:
                        self.head = None
                    else:
                        last = self.head

                        while last.next != self.head:
                            last = last.next

                        self.head = current.next
                        last.next = self.head

                else:
                    previous.next = current.next

                print("Value deleted")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found")

    def delete_first(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head

        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head

    def delete_last(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")

    def display_head_tail(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        tail = self.head

        while tail.next != self.head:
            tail = tail.next

        print("Head:", self.head.data)
        print("Tail:", tail.data)

    def display_tail_head(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        values = []
        temp = self.head

        while True:
            values.append(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        print("Tail to Head:", end=" ")

        for i in range(len(values) - 1, -1, -1):
            print(values[i], end=" ")

        print()


cll = CLL()

while True:
    print("\n--- CIRCULAR LINKED LIST ---")
    print("1. Create")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Nodes")
    print("9. Display")
    print("10. Display Head and Tail")
    print("11. Display Tail to Head")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_index()

    elif choice == 5:
        cll.delete_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        cll.display_head_tail()

    elif choice == 11:
        cll.display_tail_head()

    elif choice == 12:
        print("Program ended")
        break

    else:
        print("Invalid choice")
