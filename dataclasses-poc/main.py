from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List, ClassVar
from datetime import datetime



# 1. Basic Dataclass
print("=" * 50)
print("1. Basic Dataclass")
print("=" * 50)

@dataclass
class Person:
    """Simple dataclass with automatic __init__, __repr__, __eq__"""
    name: str
    age: int
    email: str

person1 = Person("Alice", 30, "alice@example.com")
person2 = Person("Alice", 30, "alice@example.com")
person3 = Person("Bob", 25, "bob@example.com")

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Person 1 == Person 2: {person1 == person2}")  # True (same values)
print(f"Person 1 == Person 3: {person1 == person3}")  # False
print(f"Person 1 is Person 2: {person1 is person2}")  # False (different objects)



# 2. Default Values and field()
print("\n" + "=" * 50)
print("2. Default Values and field()")
print("=" * 50)

@dataclass
class Product:
    """Dataclass with default values"""
    name: str
    price: float
    in_stock: bool = True
    tags: List[str] = field(default_factory=list)  # Mutable defaults need default_factory
    created_at: datetime = field(default_factory=datetime.now)

product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 29.99, in_stock=False, tags=["electronics", "accessories"])

print(f"Product 1: {product1}")
print(f"Product 2: {product2}")
print(f"Product 1 tags: {product1.tags}")
print(f"Product 2 tags: {product2.tags}")

# Modifying tags on product1 doesn't affect product2
product1.tags.append("computers")
print(f"After appending to product1 tags:")
print(f"Product 1 tags: {product1.tags}")
print(f"Product 2 tags: {product2.tags}")  # Unchanged



# 3. Field Metadata and Customization

print("\n" + "=" * 50)
print("3. Field Metadata and Customization")
print("=" * 50)

@dataclass
class User:
    """Dataclass with field customization"""
    username: str
    password: str = field(repr=False)  # Don't include in repr
    age: int = field(default=0)
    _internal_id: int = field(init=False, repr=False)  # Not in __init__ or __repr__
    login_count: int = field(default=0, compare=False)  # Don't use in comparisons

    def __post_init__(self):
        """Called after __init__"""
        self._internal_id = hash(self.username)
        print(f"  [__post_init__] Generated internal ID: {self._internal_id}")

user1 = User("alice", "secret123", age=30, login_count=5)
user2 = User("alice", "different_password", age=30, login_count=100)

print(f"User 1: {user1}")  # password not shown
print(f"User 1 == User 2: {user1 == user2}")  # True (login_count not compared)



# 4. Frozen Dataclasses (Immutable)

print("\n" + "=" * 50)
print("4. Frozen Dataclasses (Immutable)")
print("=" * 50)

@dataclass(frozen=True)
class Point:
    """Immutable dataclass - can't modify after creation"""
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

point = Point(3.0, 4.0)
print(f"Point: {point}")
print(f"Distance from origin: {point.distance_from_origin()}")

try:
    point.x = 5.0  # This will raise an error
except AttributeError as e:
    print(f"Error when trying to modify frozen dataclass: {e}")

# Frozen dataclasses can be used as dict keys
points_dict = {
    Point(0, 0): "origin",
    Point(1, 1): "diagonal",
}
print(f"Points dict: {points_dict}")



# 5. Ordering and Comparison

print("\n" + "=" * 50)
print("5. Ordering and Comparison")
print("=" * 50)

@dataclass(order=True)
class Score:
    """Dataclass with automatic ordering based on field order"""
    points: int
    name: str = field(compare=False)  # Don't use name in comparisons

scores = [
    Score(85, "Alice"),
    Score(92, "Bob"),
    Score(78, "Charlie"),
    Score(92, "David"),  # Same points as Bob
]

print("Unsorted scores:")
for score in scores:
    print(f"  {score}")

sorted_scores = sorted(scores)
print("\nSorted scores:")
for score in sorted_scores:
    print(f"  {score}")

print(f"\nScore(85, 'Alice') < Score(92, 'Bob'): {Score(85, 'Alice') < Score(92, 'Bob')}")



# 6. Class Variables

print("\n" + "=" * 50)
print("6. Class Variables")
print("=" * 50)

@dataclass
class Employee:
    """Dataclass with class variables"""
    name: str
    department: str
    salary: float

    company_name: ClassVar[str] = "TechCorp"  # Shared across all instances
    employee_count: ClassVar[int] = 0

    def __post_init__(self):
        Employee.employee_count += 1

emp1 = Employee("Alice", "Engineering", 100000)
emp2 = Employee("Bob", "Marketing", 80000)

print(f"Employee 1: {emp1}")
print(f"Employee 2: {emp2}")
print(f"Company name: {Employee.company_name}")
print(f"Total employees: {Employee.employee_count}")



# 7. Inheritance

print("\n" + "=" * 50)
print("7. Inheritance")
print("=" * 50)

@dataclass
class Animal:
    """Base dataclass"""
    name: str
    age: int

    def speak(self) -> str:
        return "Some sound"

@dataclass
class Dog(Animal):
    """Derived dataclass with additional fields"""
    breed: str
    is_good_boy: bool = True

    def speak(self) -> str:
        return "Woof!"

@dataclass
class Cat(Animal):
    """Another derived dataclass"""
    indoor: bool = True

    def speak(self) -> str:
        return "Meow!"

dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, indoor=True)

print(f"Dog: {dog}")
print(f"Dog speaks: {dog.speak()}")
print(f"Cat: {cat}")
print(f"Cat speaks: {cat.speak()}")



# 8. Utility Functions: asdict, astuple, replace

print("\n" + "=" * 50)
print("8. Utility Functions")
print("=" * 50)

@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str

book = Book("1984", "George Orwell", 1949, "978-0451524935")

# Convert to dict
book_dict = asdict(book)
print(f"As dict: {book_dict}")

# Convert to tuple
book_tuple = astuple(book)
print(f"As tuple: {book_tuple}")

# Create modified copy (dataclass remains unchanged)
updated_book = replace(book, year=2024)
print(f"Original book: {book}")
print(f"Updated book: {updated_book}")



# 9. Post-Init Processing

print("\n" + "=" * 50)
print("9. Post-Init Processing")
print("=" * 50)

@dataclass
class Rectangle:
    """Dataclass with computed fields in __post_init__"""
    width: float
    height: float
    area: float = field(init=False)
    perimeter: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)

rect = Rectangle(5.0, 3.0)
print(f"Rectangle: {rect}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")



# 10. InitVar - Init-only Variables

print("\n" + "=" * 50)
print("10. InitVar - Init-only Variables")
print("=" * 50)

from dataclasses import InitVar

@dataclass
class DatabaseConnection:
    """Dataclass using InitVar for parameters needed only during init"""
    host: str
    port: int
    database: str
    connection_string: str = field(init=False, repr=True)

    # InitVar fields are passed to __init__ and __post_init__ but not stored
    username: InitVar[str] = "admin"
    password: InitVar[str] = "password"

    def __post_init__(self, username: str, password: str):
        self.connection_string = f"{username}:{password}@{self.host}:{self.port}/{self.database}"

db = DatabaseConnection("localhost", 5432, "mydb", username="john", password="secret")
print(f"Database connection: {db}")
print(f"Connection string: {db.connection_string}")
print(f"Has 'username' attribute: {hasattr(db, 'username')}")
