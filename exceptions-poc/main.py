# 1. Basic try / except

print("--- Basic try/except ---")

try:
    result = 10 / 0  # Division by zero raises an exception
    print("This line won't run")
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handles the error


# 2. Multiple except blocks

print("\n--- Multiple except blocks ---")

try:
    value = int("abc")  # This raises ValueError
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid conversion to int")  # Handles this one


# 3. Handling multiple exceptions in one line

print("\n--- Multiple exceptions in one line ---")

try:
    result = 10 / int("a")
except (ZeroDivisionError, ValueError) as e:
    print("Caught an error:", e)


# 4. try / except / else

print("\n--- try / except / else ---")

try:
    num = int("5")
except ValueError:
    print("Could not convert to int")
else:
    print("Conversion successful! num =", num)
    print("Else block runs when no exception occurs.")


# 5. try / except / finally

print("\n--- try / except / finally ---")

try:
    f = open("example.txt", "w")
    f.write("Hello, World!")
    print("File written successfully.")
except IOError:
    print("Error writing to file")
finally:
    f.close()
    print("File closed (finally always runs).")


# 6. Raising exceptions manually

print("\n--- Raising exceptions manually ---")

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, 0))
except ValueError as e:
    print("Caught error:", e)


# 7. Custom exceptions

print("\n--- Custom exception example ---")

class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is not allowed."""
    def __init__(self, value):
        super().__init__(f"Negative number not allowed: {value}")
        self.value = value

def sqrt(x):
    if x < 0:
        raise NegativeNumberError(x)
    return x ** 0.5

try:
    print("Square root of 9:", sqrt(9))
    print("Square root of -1:", sqrt(-1))
except NegativeNumberError as e:
    print("Caught custom exception:", e)
finally:
    print("Computation finished (finally always runs).")
