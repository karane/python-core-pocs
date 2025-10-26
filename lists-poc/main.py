# Python Lists Example

# 1. Creation
fruits = ["apple", "banana", "cherry"]
numbers = list(range(5))  # [0, 1, 2, 3, 4]
mixed = [1, "two", 3.0, True]

print("List Creation:")
print(f"fruits = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")
print("-" * 40)

# 2. Indexing and Slicing
print("Indexing and Slicing:")
print(f"fruits[0] = {fruits[0]}")     # First element
print(f"fruits[-1] = {fruits[-1]}")   # Last element
print(f"fruits[1:3] = {fruits[1:3]}") # Slice from index 1 to 2
print(f"numbers[:3] = {numbers[:3]}") # From start to index 2
print(f"numbers[2:] = {numbers[2:]}") # From index 2 to end
print(f"numbers[::-1] = {numbers[::-1]}") # Reverse list
print("-" * 40)

# 3. Common List Methods
print("Common List Methods:")
fruits.append("date")            # Add element to end
print(f"append: {fruits}")

fruits.insert(1, "blueberry")    # Insert at position 1
print(f"insert: {fruits}")

fruits.remove("banana")          # Remove by value
print(f"remove: {fruits}")

last = fruits.pop()              # Remove and return last
print(f"pop (removed '{last}'): {fruits}")

fruits.sort()                    # Sort alphabetically
print(f"sort: {fruits}")

fruits.reverse()                 # Reverse list
print(f"reverse: {fruits}")

count_example = ["a", "b", "a", "c", "a"]
print(f"count('a'): {count_example.count('a')}")

numbers.extend([5, 6])
print(f"extend: {numbers}")
print("-" * 40)

# 4. List Comprehensions
print("List Comprehensions:")
squares = [x**2 for x in range(6)]
print(f"Squares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

words = ["hello", "python", "world"]
upper_words = [w.upper() for w in words]
print(f"Uppercase words: {upper_words}")

pairs = [(x, y) for x in range(3) for y in range(2)]
print(f"Pairs: {pairs}")
print("-" * 40)
