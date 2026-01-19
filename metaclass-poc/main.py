# Step 1: Create a custom metaclass
class UpperCaseMetaclass(type):
    def __new__(mcls, name, bases, attrs):
        new_attrs = {}

        for key, value in attrs.items():
            # Do not modify special methods (__init__, __str__, etc.)
            if key.startswith("__") and key.endswith("__"):
                new_attrs[key] = value
            else:
                # Convert attribute names to uppercase
                new_attrs[key.upper()] = value

        # Create the new class with modified attributes
        return super().__new__(mcls, name, bases, new_attrs)


# Step 2: Create a class using the metaclass
class Person(metaclass=UpperCaseMetaclass):
    age = 30

    def say_hello(self):
        return "Hello!"


# Step 3: Using the class
p = Person()

print(dir(p))         # Notice SAY_HELLO instead of say_hello
print()
print(p.SAY_HELLO())  # Works
