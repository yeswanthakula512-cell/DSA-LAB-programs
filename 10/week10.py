
class Hashing:

    def __init__(self, size):
        self.size = size
        self.chain = [[] for i in range(size)]
        self.linear = [None] * size
        self.quadratic = [None] * size

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Separate Chaining
    def insert_chaining(self, key):
        index = self.hash_function(key)

        if key not in self.chain[index]:
            self.chain[index].append(key)

    # Linear Probing
    def insert_linear(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] is None:
                self.linear[pos] = key
                return

            elif self.linear[pos] == key:
                print("Duplicate value")
                return

        print("Hash table is full")

    # Quadratic Probing
    def insert_quadratic(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] is None:
                self.quadratic[pos] = key
                return

            elif self.quadratic[pos] == key:
                print("Duplicate value")
                return

        print("No empty position found")

    # Search using Separate Chaining
    def search_chaining(self, key):
        index = self.hash_function(key)

        return key in self.chain[index]

    # Search using Linear Probing
    def search_linear(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] is None:
                return False

            if self.linear[pos] == key:
                return True

        return False

    # Search using Quadratic Probing
    def search_quadratic(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] is None:
                return False

            if self.quadratic[pos] == key:
                return True

        return False

    # Display Separate Chaining
    def display_chaining(self):
        print("\nSeparate Chaining:")

        for i in range(self.size):
            print(i, ":", self.chain[i])

    # Display Linear Probing
    def display_linear(self):
        print("\nLinear Probing:")

        for i in range(self.size):
            print(i, ":", self.linear[i])

    # Display Quadratic Probing
    def display_quadratic(self):
        print("\nQuadratic Probing:")

        for i in range(self.size):
            print(i, ":", self.quadratic[i])


# Main

h = Hashing(11)

values = [21, 32, 43, 54, 65, 76]

for value in values:
    h.insert_chaining(value)
    h.insert_linear(value)
    h.insert_quadratic(value)

h.display_chaining()
h.display_linear()
h.display_quadratic()

print("\nSearch 43:")

print("Separate Chaining:", h.search_chaining(43))
print("Linear Probing:", h.search_linear(43))
print("Quadratic Probing:", h.search_quadratic(43))
