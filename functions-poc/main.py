# =========================================
# Function definitions
# =========================================
def greet(name):
    """Return a greeting message for a given name."""
    return f"Hello, {name}!"


def describe_person(name, age=30, city="Unknown"):
    """
    Demonstrates positional arguments, keyword arguments, and default values.
    """
    return f"{name} is {age} years old and lives in {city}."


def summarize(*args, **kwargs):
    """
    Demonstrates variable-length arguments (*args, **kwargs)
    Returns the sum of all numeric arguments.
    """
    print("Positional args:", args)
    print("Keyword args:", kwargs)
    total = sum(args) if args else 0
    return total + sum(kwargs.values())


def apply_operation(x, y, func):
    """Applies a function 'func' to arguments x and y."""
    return func(x, y)


# =========================================
# Lambda functions
# =========================================
square = lambda x: x ** 2
add = lambda x, y: x + y


# =========================================
# Main function
# =========================================
def main():
    print(greet("Alice"))
    
    print(describe_person("Bob"))
    print(describe_person(name="Carol", age=25, city="Paris"))
    print(describe_person("Dave", city="London"))
    
    total = summarize(1, 2, 3, a=4, b=5)
    print("Total sum:", total)
    
    print("Square of 5:", square(5))
    print("Add 3 + 7:", add(3, 7))
    
    result = apply_operation(4, 5, lambda a, b: a * b)
    print("4 * 5 using lambda in apply_operation:", result)


if __name__ == "__main__":
    main()
