# 1. STRINGS AS SEQUENCES

text = "Hello, World!"

# Strings are sequences — they support indexing, slicing, and iteration.
print("Original text:", text)
print("First character:", text[0])          # Indexing
print("Last 6 characters:", text[-6:])      # Slicing
print("Characters in reverse:", text[::-1]) # Reversed slice

# Iterate over a string (sequence)
print("Characters one by one:")
for ch in text:
    print(ch, end=" ")
print("\n")


# 2. ITERATORS & GENERATORS

# Any iterable (like a list, tuple, or string) can produce an iterator
nums = [1, 2, 3, 4]
it = iter(nums)

print("Using an iterator:")
print(next(it))  # 1
print(next(it))  # 2

# Generators are functions that yield values lazily (on demand)
def squares(limit):
    """Generator that yields square numbers up to limit."""
    for i in range(1, limit + 1):
        yield i * i  # 'yield' produces a sequence lazily

print("Squares from generator:")
for sq in squares(5):
    print(sq, end=" ")
print("\n")


# 3. NESTED DATA STRUCTURES

# Nested structures combine lists, dicts, and tuples
students = [
    {
        "name": "Alice",
        "scores": {"math": 85, "english": 90, "science": 88}
    },
    {
        "name": "Bob",
        "scores": {"math": 78, "english": 82, "science": 89}
    }
]

# Accessing nested data
print("Alice's math score:", students[0]["scores"]["math"])

# Iterating through nested data
print("Average scores:")
for student in students:
    scores = student["scores"].values()
    avg = sum(scores) / len(scores)
    print(f"{student['name']} -> {avg:.1f}")

# Nested comprehension example:
all_scores = [score for s in students for score in s["scores"].values()]
print("All scores flattened:", all_scores)
