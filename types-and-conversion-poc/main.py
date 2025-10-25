# === Primitive Data Types and Type Conversion in Python ===

# 1. Integer (int)
age = 30
year = 2025
print("Integer examples:")
print("Age:", age, "| Type:", type(age))
print("Year:", year, "| Type:", type(year))
print("Addition:", age + 5)
print()

# 2. Floating-point number (float)
height = 1.75
weight = 68.5
print("Float examples:")
print("Height:", height, "| Type:", type(height))
print("Weight:", weight, "| Type:", type(weight))
print("BMI (approx):", weight / (height ** 2))
print()

# 3. Boolean (bool)
is_adult = True
has_license = False
print("Boolean examples:")
print("Is adult:", is_adult, "| Type:", type(is_adult))
print("Has license:", has_license, "| Type:", type(has_license))
print("Can drive:", is_adult and has_license)
print()

# 4. String (str)
name = "Alice"
greeting = f"Hello, {name}!"
print("String examples:")
print("Name:", name, "| Type:", type(name))
print("Greeting:", greeting)
print("Uppercase:", name.upper())
print("Length of name:", len(name))
print()

# 5. NoneType (None)
middle_name = None
print("NoneType example:")
print("Middle name:", middle_name, "| Type:", type(middle_name))
print("Is middle name defined?", middle_name is not None)
print()

# === Type Conversion (Casting) ===
print("Type Conversion Examples:")

# Convert int to float
age_float = float(age)
print("int -> float:", age_float, "| Type:", type(age_float))

# Convert float to int (fractional part is discarded)
height_int = int(height)
print("float -> int:", height_int, "| Type:", type(height_int))

# Convert int to string
year_str = str(year)
print("int -> str:", year_str, "| Type:", type(year_str))

# Convert string to int
num_str = "42"
num_int = int(num_str)
print("str -> int:", num_int, "| Type:", type(num_int))

# Convert boolean to int
print("bool -> int:", int(is_adult), "| Type:", type(int(is_adult)))

# Convert int to bool (0 is False, others are True)
print("int -> bool:", bool(0), "|", bool(10))
print()

# === Summary ===
print("Summary of final variable types:")
print("age: ", type(age)), 
print("height: ", type(height))
print("is_adult: ", type(is_adult))
print("name: ", type(name))
print("middle_name: ", type(middle_name))
