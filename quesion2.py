class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

booking_queue = Queue()
booking_queue.enqueue("Booking 1")
booking_queue.enqueue("Booking 2")
booking_queue.enqueue("Booking 3")
print(booking_queue.dequeue()) 
print(booking_queue.dequeue()) 
print(booking_queue.size()) 

#circular queue
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = self.tail = -1
        self.capacity = capacity

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.head = 0

        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        result = self.queue[self.head]
        self.queue[self.head] = None

        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity

        return result

    def size(self):
        if self.is_empty():
            return 0
        
        if self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.capacity - (self.head - self.tail - 1)

# Example usage
circular_queue = CircularQueue(3)

# Adding bookings to the circular queue (enqueue)
circular_queue.enqueue("Booking 1")
circular_queue.enqueue("Booking 2")
circular_queue.enqueue("Booking 3")

circular_queue.enqueue("Booking 4") 
print(circular_queue.dequeue())  
print(circular_queue.dequeue())  
circular_queue.enqueue("Booking 4")
print(circular_queue.size()) 

