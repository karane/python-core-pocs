# 1. TUPLES
print("\n=== TUPLES ===")

# Creation
person = ("Alice", 30, "Engineer")
print(f"person = {person}")

# Indexing
print(f"person[0] = {person[0]}")  # Access by index

# Immutability demonstration
try:
    person[1] = 31
except TypeError as e:
    print(f"Tuples are immutable: {e}")

# Packing and Unpacking
data = ("Bob", 25, "Developer")
name, age, job = data  # Unpacking
print(f"Unpacked -> name={name}, age={age}, job={job}")

# Tuple without parentheses (packing)
point = 10, 20
x, y = point
print(f"Packed as tuple: {point}, unpacked -> x={x}, y={y}")
print("-" * 40)


# 2. SETS
print("\n=== SETS ===")

# Creation (unordered, unique elements)
set_a = {1, 2, 3, 3, 4}
set_b = set([3, 4, 5, 6])
print(f"set_a = {set_a}")
print(f"set_b = {set_b}")

# Basic methods
set_a.add(5)
print(f"After add(5): {set_a}")

set_a.discard(1)
print(f"After discard(1): {set_a}")

set_a.update([6, 7])
print(f"After update([6, 7]): {set_a}")

print(f"len(set_a) = {len(set_a)}")

# Set operations
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")

# Membership
print(f"3 in set_a -> {3 in set_a}")
print(f"9 not in set_b -> {9 not in set_b}")
print("-" * 40)


# 3. DICTIONARIES
print("\n=== DICTIONARIES ===")

# Creation
person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}
print(f"person = {person}")

# Accessing values
print(f"Name: {person['name']}")
print(f"Age (using get): {person.get('age')}")

# Updating values
person["age"] = 31
person.update({"City": "New York"})
print(f"After updates: {person}")

# Removing items
removed = person.pop("job")
print(f"Removed 'job': {removed}, remaining: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iteration
print("Iterating over dictionary:")
for key, value in person.items():
    print(f"{key} -> {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Dictionary comprehension (squares): {squares}")
print("-" * 40)
