def counting_sort(bookings, max_priority):
    # Create a count array to store count of individual priorities
    count = [0] * (max_priority + 1)
    output = [None] * len(bookings)
    
    # Store count of each priority
    for booking in bookings:
        count[booking["priority"]] += 1

    # Change count[i] so it contains the position of 
    # this priority in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output booking array
    for booking in reversed(bookings):
        output[count[booking["priority"]] - 1] = booking
        count[booking["priority"]] -= 1

    return output

# Example usage
bookings = [
    {"name": "Booking 1", "priority": 3},
    {"name": "Booking 2", "priority": 1},
    {"name": "Booking 3", "priority": 4},
    {"name": "Booking 4", "priority": 2},
    {"name": "Booking 5", "priority": 3}
]

# Assume the highest priority is 4
max_priority = 4

sorted_bookings = counting_sort(bookings, max_priority)
for booking in sorted_bookings:
    print(f"{booking['name']} - Priority {booking['priority']}")
