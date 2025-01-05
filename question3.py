class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete_first(self):
        if self.is_empty():
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp.data

    def delete_last(self):
        if self.is_empty():
            return None
        temp = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp.data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage
booking_list = DoublyLinkedList()

# Adding bookings to the list (append)
booking_list.append("Booking 1")
booking_list.append("Booking 2")
booking_list.append("Booking 3")

# Display bookings forward
booking_list.display_forward()  # Output: Booking 1 Booking 2 Booking 3

# Removing the first booking
print(booking_list.delete_first())  # Output: Booking 1

# Adding a booking at the start (prepend)
booking_list.prepend("Booking 0")

# Display bookings backward
booking_list.display_backward()  # Output: Booking 3 Booking 2 Booking 0

# Removing the last booking
print(booking_list.delete_last())  # Output: Booking 3

# Check the current bookings
booking_list.display_forward()  # Output: Booking 0 Booking 2
