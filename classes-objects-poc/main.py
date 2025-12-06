# Base class
class Person:
    # Constructor (__init__) initializes instance attributes
    def __init__(self, name, age):
        self.name = name      # public attribute
        self._age = age       # "protected" (by convention)
    
    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self._age} years old.")
    
    # Getter and setter for encapsulation
    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive.")


# Derived class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the parent constructor
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    # Method to add a course
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    # Method overriding (redefining greet)
    def greet(self):
        print(f"Hi, I'm {self.name}, a student with ID {self.student_id}.")


# Another class (no inheritance)
class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def describe(self):
        print(f"Course {self.code}: {self.title}")


def main():
    # Create objects (instances)
    alice = Person("Alice", 30)
    bob = Student("Bob", 20, "S123")
    math = Course("MATH101", "Calculus I")

    # Access methods and attributes
    alice.greet()
    bob.greet()
    math.describe()

    # Demonstrate encapsulation
    print(f"{alice.name}'s age is {alice.get_age()}")
    alice.set_age(31)
    print(f"{alice.name}'s new age is {alice.get_age()}")

    # Demonstrate inheritance and method overriding
    bob.enroll("Physics")
    bob.enroll("Computer Science")
    print(f"{bob.name}'s courses:", bob.courses)


if __name__ == "__main__":
    main()
