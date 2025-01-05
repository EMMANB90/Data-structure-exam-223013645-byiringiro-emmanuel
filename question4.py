class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.size == self.max_size

    def append(self, data):
        if self.is_full():
            print("List is full")
            return

        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            return None

        temp = self.head
        self.head = self.head.next
        if self.head is None:  # List becomes empty
            self.tail = None
        self.size -= 1
        return temp.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
order_list = SinglyLinkedList(max_size=3)

# Adding orders to the linked list (append) until it reaches max size
order_list.append("Order 1")
order_list.append("Order 2")
order_list.append("Order 3")

# Trying to add another order to a full list
order_list.append("Order 4")  # Output: List is full

# Displaying current orders
order_list.display()  # Output: Order 1 Order 2 Order 3

# Removing the first order
print(order_list.delete_first())  # Output: Order 1

# Adding a new order after removing one
order_list.append("Order 4")

# Displaying updated orders
order_list.display()  # Output: Order 2 Order 3 Order 4