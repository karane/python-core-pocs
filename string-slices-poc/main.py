# Python Strings Example

# ---------------------------------
# 1. String Slicing
# ---------------------------------
text = "Hello, Python!"

print("String Slicing:")
print(f"text = '{text}'")
print(f"text[0] = {text[0]}")        # First character
print(f"text[-1] = {text[-1]}")      # Last character
print(f"text[0:5] = {text[0:5]}")    # Slice from index 0 to 4
print(f"text[7:] = {text[7:]}")      # From index 7 to end
print(f"text[:5] = {text[:5]}")      # From start to index 4
print(f"text[::2] = {text[::2]}")    # Every 2nd character
print(f"text[::-1] = {text[::-1]}")  # Reverse string
print("-" * 40)

# ---------------------------------
# 2. String Formatting (old and new)
# ---------------------------------
name = "Alice"
age = 30
lang = "Python"

print("String Formatting:")
# Old style
print("My name is %s and I am %d years old." % (name, age))
# str.format() method
print("My name is {} and I love {}.".format(name, lang))
print("My name is {0} and I love {1}.".format(name, lang))
print("My name is {name} and I love {language}.".format(name=name, language=lang))
print("-" * 40)

# ---------------------------------
# 3. f-Strings (modern and clean)
# ---------------------------------
print("F-Strings:")
print(f"My name is {name}, I’m {age} years old, and I code in {lang}.")
print(f"Next year I’ll be {age + 1}.")
print(f"Uppercased language: {lang.upper()}")
print("-" * 40)

# ---------------------------------
# 4. Common String Methods
# ---------------------------------
sentence = "  Python is fun and powerful!  "

print("String Methods:")
print(f"Original: '{sentence}'")
print(f"strip(): '{sentence.strip()}'")       # Remove leading/trailing spaces
print(f"lower(): '{sentence.lower()}'")       # Lowercase
print(f"upper(): '{sentence.upper()}'")       # Uppercase
print(f"replace(): '{sentence.replace('fun', 'awesome')}'")  # Replace substring
print(f"split(): {sentence.split()}")         # Split by spaces
print(f"split('a'): {sentence.split('a')}")   # Split by 'a'
words = ["Python", "is", "awesome"]
print(f"join(): {' '.join(words)}")           # Join with space
print(f"count('o'): {sentence.count('o')}")   # Count occurrences
print(f"startswith('  Py'): {sentence.startswith('  Py')}")
print(f"endswith('!  '): {sentence.endswith('!  ')}")
print("-" * 40)

# ---------------------------------
# 5. Checking characters
# ---------------------------------
sample = "Python3"

print("Character Checks:")
print(f"isalnum(): {sample.isalnum()}")  # Letters + digits only
print(f"isalpha(): {sample.isalpha()}")  # Letters only
print(f"isdigit(): {'123'.isdigit()}")   # Digits only
print(f"isspace(): {'   '.isspace()}")   # Spaces only
