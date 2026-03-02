# Take input and store in a Tuple
numbers = tuple(map(int, input("Enter a series of integers (space-separated): ").split()))

print("\nOriginal Tuple:", numbers)

# a) Total number of items
print("\na) Total number of items:", len(numbers))

# b) Last item
print("b) Last item:", numbers[-1])

# c) Reverse order
print("c) Tuple in reverse order:", numbers[::-1])

# d) Check if 5 exists
if 5 in numbers:
    print("d) Yes (Tuple contains 5)")
else:
    print("d) No (Tuple does not contain 5)")

# e) Remove first and last, sort remaining
remaining = sorted(numbers[1:-1])
print("e) After removing first & last, sorted:", tuple(remaining))