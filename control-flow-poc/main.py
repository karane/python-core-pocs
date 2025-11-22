# =============================================
# 1. if, elif, else
# =============================================

x = 42

if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif 0 < x < 10:
    print("Small positive number")
else:
    print("Large number")  # This will print


# =============================================
# 2. Loops: for, while, break, continue, else
# =============================================

print("\n--- For loop with break and else ---")
for i in range(5):
    if i == 3:
        print("Breaking at", i)
        break
    print("i =", i)
else:
    print("Loop completed normally (no break)")  # This won't execute

print("\n--- For loop with continue ---")
for i in range(5):
    if i == 2:
        continue  # Skip printing when i == 2
    print("i =", i)

print("\n--- While loop with else ---")
count = 0
while count < 3:
    print("count =", count)
    count += 1
else:
    print("While loop ended normally (no break)")  # Executes when no break

print("\n--- While loop with break ---")
count = 0
while count < 5:
    if count == 3:
        print("Breaking at", count)
        break
    print("count =", count)
    count += 1
else:
    print("This won't print because of the break")


# =============================================
# 3. Comprehensions: list, dict, set
# =============================================

print("\n--- List comprehension ---")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers if n % 2 == 1]  # squares of odd numbers
print("Squares of odd numbers:", squares)

print("\n--- Dict comprehension ---")
square_map = {n: n**2 for n in numbers}
print("Number to square mapping:", square_map)

print("\n--- Set comprehension ---")
unique_lengths = {len(word) for word in ["apple", "banana", "pear", "apple"]}
print("Unique word lengths:", unique_lengths)


# =============================================
# 4. pass and del
# =============================================

print("\n--- pass example ---")
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    else:
        print("Processing i =", i)

print("\n--- del example ---")
data = [10, 20, 30, 40]
print("Before del:", data)
del data[1]  # Delete element at index 1
print("After del:", data)

person = {"name": "Alice", "age": 30}
print("Before del:", person)
del person["age"]  # Delete key from dict
print("After del:", person)
