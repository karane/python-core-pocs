class Employee:
    company_name = "TechCorp" 

    def __init__(self, name, salary):
        self.name = name        
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise! New salary: ${self.salary}")

    # Class method: works with the class itself
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    # Static method: utility function not tied to instance or class
    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


# Example usage
# Instance methods
alice = Employee("Alice", 50000)
bob = Employee("Bob", 60000)

alice.give_raise(5000)
bob.give_raise(3000)

# Class method
Employee.change_company_name("MegaTech")

print(f"Alice works at {alice.company_name}")
print(f"Bob works at {bob.company_name}")

# Static method
print(Employee.is_valid_salary(1000))  # True
print(Employee.is_valid_salary(-500))  # False
