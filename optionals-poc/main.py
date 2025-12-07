from typing import Optional


# 1. Optional return type: function return int or None
def find_user_age(name: str) -> Optional[int]:
    users = {"Ana": 30, "Bruno": 25}
    return users.get(name)  # may return None


# 2. Optional parameter with default None
def greet(name: Optional[str] = None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")


# 3. Optional inside a class
class User:
    def __init__(self, name: str, nickname: Optional[str] = None):
        self.name = name
        self.nickname = nickname

    def display(self):
        if self.nickname:
            print(f"{self.name} ({self.nickname})")
        else:
            print(self.name)


# 4. Optional safety example: avoid NoneType errors
def get_domain(email: Optional[str]) -> Optional[str]:
    if email is None:
        return None
    if "@" not in email:
        return None
    return email.split("@")[1]


# 5. Practical config example
def load_port(env_port: Optional[str]) -> int:
    if env_port is None:
        return 8080  # default port
    return int(env_port)


def main():
    print("\n=== 1. Optional return example ===")
    age = find_user_age("Carlos")
    if age is None:
        print("User not found.")
    else:
        print(f"Age is {age}")

    age = find_user_age("Ana")
    print("Ana age:", age)

    print("\n=== 2. Optional parameter example ===")
    greet()
    greet("Karane")

    print("\n=== 3. Optional inside a class ===")
    u1 = User("Marcos")
    u2 = User("Julia", "Juju")
    u1.display()
    u2.display()

    print("\n=== 4. Safe access with Optional ===")
    print("domain:", get_domain("user@example.com"))
    print("domain:", get_domain(None))
    print("domain:", get_domain("invalid-email"))

    print("\n=== 5. Optional in config example ===")
    print("port:", load_port(None))
    print("port:", load_port("9090"))


if __name__ == "__main__":
    main()