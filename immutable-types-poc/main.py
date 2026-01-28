from dataclasses import dataclass, replace
from typing import Tuple, FrozenSet


def separator(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


def main():
    # BASIC IMMUTABLE TYPES
    separator("BASIC IMMUTABLE TYPES")

    i = 42
    f = 3.14
    s = "hello"
    t = (1, 2, 3)
    fs = frozenset({1, 2, 3})

    print("int:", i)
    print("float:", f)
    print("str:", s)
    print("tuple:", t)
    print("frozenset:", fs)

    # Strings are immutable
    new_s = s.upper()
    print("Original string:", s)
    print("New string:", new_s)

    # MUTABLE VS IMMUTABLE
    separator("MUTABLE VS IMMUTABLE")

    mutable_list = [1, 2, 3]
    immutable_tuple = (1, 2, 3)

    mutable_list.append(4)
    print("Mutable list after append:", mutable_list)

    try:
        immutable_tuple.append(4)  # type: ignore
    except AttributeError as e:
        print("Tuple mutation error:", e)

    # SHALLOW IMMUTABILITY
    separator("SHALLOW IMMUTABILITY")

    mixed = (1, [2, 3])
    print("Before:", mixed)

    mixed[1].append(4)
    print("After modifying inner list:", mixed)

    print("Tuple is immutable, inner list is not")

    # FUNCTIONAL UPDATE PATTERN
    separator("FUNCTIONAL UPDATE")

    user = ("Alice", 30)
    print("Original user:", user)

    updated_user = (user[0], user[1] + 1)
    print("Updated user:", updated_user)

    # TUPLE AS RECORD
    separator("TUPLE AS RECORD")

    Point = Tuple[int, int]
    p1: Point = (10, 20)
    print("Point:", p1)

    p2 = (p1[0] + 5, p1[1] + 5)
    print("Moved point:", p2)

    # FROZENSET
    separator("FROZENSET")

    permissions: FrozenSet[str] = frozenset({"read", "write"})
    print("Permissions:", permissions)

    role_map = {
        frozenset({"read"}): "GUEST",
        frozenset({"read", "write"}): "USER",
        frozenset({"read", "write", "delete"}): "ADMIN",
    }

    print("Role:", role_map[permissions])

    # FROZEN DATACLASS
    separator("FROZEN DATACLASS")

    @dataclass(frozen=True)
    class User:
        name: str
        age: int
        email: str

    user = User("Alice", 30, "alice@example.com")
    print("User:", user)

    try:
        user.age = 31  # type: ignore
    except Exception as e:
        print("Mutation error:", e)

    updated_user = replace(user, age=31)
    print("Updated user:", updated_user)

    # IMMUTABILITY + CACHING
    separator("IMMUTABILITY + CACHING")

    cache = {}

    def expensive_calculation(config):
        if config in cache:
            print("Cache hit!")
            return cache[config]

        print("Computing...")
        result = sum(config)
        cache[config] = result
        return result

    config1 = (1, 2, 3)
    config2 = (1, 2, 3)

    print(expensive_calculation(config1))
    print(expensive_calculation(config2))


if __name__ == "__main__":
    main()
