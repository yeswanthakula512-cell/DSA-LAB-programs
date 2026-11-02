
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = value
            print(value, "inserted into the queue")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Circular Queue Underflow")
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None

            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

            print(value, "deleted from the queue")

    # Peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("The elements of the queue are:")
            i = self.front

            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size


size = int(input("Enter the size of the queue: "))
q = CircularQueue(size)

while True:
    print("\n----- CIRCULAR QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Peek")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the element to enqueue: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        q.peek()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice")
