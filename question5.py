class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def display(self):
        for item in reversed(self.items):
            print(item)

# Example usage
booking_stack = Stack()

# Adding bookings to the stack (push)
booking_stack.push("Booking 1")
booking_stack.push("Booking 2")
booking_stack.push("Booking 3")

# Displaying the current stack
print("Current bookings in the stack:")
booking_stack.display()  # Output: Booking 3, Booking 2, Booking 1

# Removing the most recent booking (pop)
print("\nMost recent booking removed:", booking_stack.pop())  # Output: Booking 3

# Viewing the next booking to be processed (peek)
print("\nNext booking to be processed:", booking_stack.peek())  # Output: Booking 2

# Displaying the updated stack
print("\nUpdated bookings in the stack:")
booking_stack.display()  # Output: Booking 2, Booking 1
