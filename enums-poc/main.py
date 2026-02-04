from enum import Enum, IntEnum, Flag, IntFlag, auto, unique
import sys

# Check Python version for StrEnum (3.11+)
if sys.version_info >= (3, 11):
    from enum import StrEnum
    HAS_STRENUM = True
else:
    HAS_STRENUM = False



# 1. Basic Enum

print("=" * 50)
print("1. Basic Enum")
print("=" * 50)

class Color(Enum):
    """Simple enumeration with explicit values"""
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(f"Color.RED: {Color.RED}")
print(f"Color.RED.name: {Color.RED.name}")
print(f"Color.RED.value: {Color.RED.value}")

# Different ways to access enum members
print(f"\nAccessing by name: Color['GREEN'] = {Color['GREEN']}")
print(f"Accessing by value: Color(2) = {Color(2)}")

# Identity and equality
print(f"\nColor.RED is Color.RED: {Color.RED is Color.RED}")
print(f"Color.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED == Color.BLUE: {Color.RED == Color.BLUE}")

# Iterating over enum
print("\nAll colors:")
for color in Color:
    print(f"  {color.name} = {color.value}")



# 2. auto() - Automatic Values

print("\n" + "=" * 50)
print("2. auto() - Automatic Values")
print("=" * 50)

class Status(Enum):
    """Enum using auto() for automatic value assignment"""
    PENDING = auto()    # 1
    RUNNING = auto()    # 2
    COMPLETED = auto()  # 3
    FAILED = auto()     # 4

print("Status values (auto-generated):")
for status in Status:
    print(f"  {status.name} = {status.value}")

# Using enums in logic
def process_task(status: Status):
    if status == Status.PENDING:
        return "Task is waiting to start"
    elif status == Status.RUNNING:
        return "Task is in progress"
    elif status == Status.COMPLETED:
        return "Task finished successfully"
    elif status == Status.FAILED:
        return "Task encountered an error"

print(f"\n{process_task(Status.RUNNING)}")
print(f"{process_task(Status.COMPLETED)}")



# 3. IntEnum - Integer Enumeration

print("\n" + "=" * 50)
print("3. IntEnum - Integer Enumeration")
print("=" * 50)

class Priority(IntEnum):
    """IntEnum members are also integers"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# IntEnum members can be compared with integers
print(f"Priority.HIGH: {Priority.HIGH}")
print(f"Priority.HIGH == 3: {Priority.HIGH == 3}")
print(f"Priority.HIGH > Priority.MEDIUM: {Priority.HIGH > Priority.MEDIUM}")
print(f"Priority.HIGH > 2: {Priority.HIGH > 2}")

# Can be used in arithmetic (though not recommended)
print(f"Priority.HIGH + 1 = {Priority.HIGH + 1}")

# Sorting
priorities = [Priority.CRITICAL, Priority.LOW, Priority.MEDIUM]
print(f"Original: {priorities}")
print(f"Sorted: {sorted(priorities)}")



# 4. StrEnum - String Enumeration (Python 3.11+)

print("\n" + "=" * 50)
print("4. StrEnum - String Enumeration (Python 3.11+)")
print("=" * 50)

if HAS_STRENUM:
    class Environment(StrEnum):
        """StrEnum members are also strings"""
        DEVELOPMENT = auto()  # Automatically becomes 'development'
        STAGING = auto()      # Automatically becomes 'staging'
        PRODUCTION = auto()   # Automatically becomes 'production'

    print(f"Environment.PRODUCTION: {Environment.PRODUCTION}")
    print(f"Environment.PRODUCTION == 'production': {Environment.PRODUCTION == 'production'}")
    print(f"Environment.PRODUCTION.upper(): {Environment.PRODUCTION.upper()}")

    # Can be used directly as strings
    config_file = f"config.{Environment.PRODUCTION}.json"
    print(f"Config file: {config_file}")
else:
    print("StrEnum is not available (requires Python 3.11+)")
    print("Alternative - using str and Enum:")

    class Environment(str, Enum):
        DEVELOPMENT = "development"
        STAGING = "staging"
        PRODUCTION = "production"

    print(f"Environment.PRODUCTION: {Environment.PRODUCTION}")
    print(f"Environment.PRODUCTION == 'production': {Environment.PRODUCTION == 'production'}")



# 5. Flag - Bitwise Combinations

print("\n" + "=" * 50)
print("5. Flag - Bitwise Combinations")
print("=" * 50)

class Permission(Flag):
    """Flag enum for bitwise operations"""
    READ = auto()     # 1 (binary: 001)
    WRITE = auto()    # 2 (binary: 010)
    EXECUTE = auto()  # 4 (binary: 100)

# Combining flags with bitwise OR
admin_perms = Permission.READ | Permission.WRITE | Permission.EXECUTE
user_perms = Permission.READ | Permission.WRITE

print(f"Admin permissions: {admin_perms}")
print(f"User permissions: {user_perms}")

# Checking flags with bitwise AND
print(f"\nAdmin has READ? {bool(admin_perms & Permission.READ)}")
print(f"Admin has EXECUTE? {bool(admin_perms & Permission.EXECUTE)}")
print(f"User has EXECUTE? {bool(user_perms & Permission.EXECUTE)}")

# Checking membership with 'in'
print(f"\nREAD in admin_perms? {Permission.READ in admin_perms}")
print(f"EXECUTE in user_perms? {Permission.EXECUTE in user_perms}")

# Removing permissions
restricted_perms = admin_perms & ~Permission.EXECUTE
print(f"\nAdmin permissions without EXECUTE: {restricted_perms}")



# 6. IntFlag - Integer Flag

print("\n" + "=" * 50)
print("6. IntFlag - Integer Flag")
print("=" * 50)

class FileMode(IntFlag):
    """IntFlag combines Flag behavior with integer operations"""
    READ = 4    # r--
    WRITE = 2   # -w-
    EXECUTE = 1 # --x

# Can combine like Flag
full_mode = FileMode.READ | FileMode.WRITE | FileMode.EXECUTE
print(f"Full mode: {full_mode} (value: {full_mode.value})")

# Can also compare with integers
print(f"Full mode == 7: {full_mode == 7}")
print(f"READ | WRITE == 6: {(FileMode.READ | FileMode.WRITE) == 6}")



# 7. @unique Decorator

print("\n" + "=" * 50)
print("7. @unique Decorator")
print("=" * 50)

# Without @unique, aliases are allowed
class HttpStatus(Enum):
    OK = 200
    SUCCESS = 200  # Alias for OK
    NOT_FOUND = 404

print("HttpStatus (aliases allowed):")
print(f"  OK: {HttpStatus.OK}")
print(f"  SUCCESS: {HttpStatus.SUCCESS}")
print(f"  OK is SUCCESS: {HttpStatus.OK is HttpStatus.SUCCESS}")

# With @unique, no aliases allowed
try:
    @unique
    class StrictHttpStatus(Enum):
        OK = 200
        SUCCESS = 200  # This will raise an error
        NOT_FOUND = 404
except ValueError as e:
    print(f"\n@unique prevents aliases: {e}")

# Correct usage of @unique
@unique
class ErrorCode(Enum):
    INVALID_INPUT = 1001
    DATABASE_ERROR = 1002
    NETWORK_ERROR = 1003
    AUTHENTICATION_FAILED = 1004

print("\nErrorCode (all values unique):")
for code in ErrorCode:
    print(f"  {code.name} = {code.value}")



# 8. Enum Methods and Properties

print("\n" + "=" * 50)
print("8. Enum Methods and Properties")
print("=" * 50)

class Planet(Enum):
    """Enum with additional data and methods"""
    MERCURY = (3.303e23, 2.4397e6)
    VENUS = (4.869e24, 6.0518e6)
    EARTH = (5.976e24, 6.37814e6)
    MARS = (6.421e23, 3.3972e6)

    def __init__(self, mass, radius):
        self.mass = mass  # kg
        self.radius = radius  # meters

    @property
    def surface_gravity(self):
        """Calculate surface gravity"""
        G = 6.67430e-11  # Gravitational constant
        return G * self.mass / (self.radius ** 2)

print("Planets:")
for planet in Planet:
    print(f"  {planet.name}: mass={planet.mass:.2e} kg, "
          f"radius={planet.radius:.2e} m, "
          f"gravity={planet.surface_gravity:.2f} m/s²")



# 9. Functional API

print("\n" + "=" * 50)
print("9. Functional API")
print("=" * 50)

# Creating enum dynamically
Direction = Enum('Direction', ['NORTH', 'SOUTH', 'EAST', 'WEST'])

print("Direction (created with functional API):")
for direction in Direction:
    print(f"  {direction.name} = {direction.value}")

# With explicit values
Size = Enum('Size', {'SMALL': 1, 'MEDIUM': 2, 'LARGE': 3})
print("\nSize (with explicit values):")
for size in Size:
    print(f"  {size.name} = {size.value}")



# 10. Enums in Practice

print("\n" + "=" * 50)
print("10. Enums in Practice")
print("=" * 50)

class OrderStatus(Enum):
    """Real-world example: Order status tracking"""
    DRAFT = "draft"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

    def can_transition_to(self, new_status: 'OrderStatus') -> bool:
        """Define valid status transitions"""
        transitions = {
            OrderStatus.DRAFT: [OrderStatus.PENDING, OrderStatus.CANCELLED],
            OrderStatus.PENDING: [OrderStatus.CONFIRMED, OrderStatus.CANCELLED],
            OrderStatus.CONFIRMED: [OrderStatus.SHIPPED, OrderStatus.CANCELLED],
            OrderStatus.SHIPPED: [OrderStatus.DELIVERED],
            OrderStatus.DELIVERED: [],
            OrderStatus.CANCELLED: [],
        }
        return new_status in transitions.get(self, [])

    @property
    def is_terminal(self) -> bool:
        """Check if this is a final status"""
        return self in (OrderStatus.DELIVERED, OrderStatus.CANCELLED)

# Simulating order workflow
current_status = OrderStatus.DRAFT
print(f"Current status: {current_status.value}")

next_status = OrderStatus.PENDING
if current_status.can_transition_to(next_status):
    print(f"Can transition to {next_status.value}: Yes")
    current_status = next_status
else:
    print(f"Can transition to {next_status.value}: No")

print(f"Is terminal status? {current_status.is_terminal}")

