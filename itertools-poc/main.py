import itertools
import operator


def separator(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


def main():
    # INFINITE ITERATORS
    separator("INFINITE ITERATORS")

    # count(start, step)
    print("count(start=10, step=2):")
    for n in itertools.islice(itertools.count(10, 2), 5):
        print(n, end=" ")
    print()

    # cycle(iterable)
    print("\ncycle(['A', 'B', 'C']):")
    for x in itertools.islice(itertools.cycle(["A", "B", "C"]), 7):
        print(x, end=" ")
    print()

    # repeat(value, times)
    print("\nrepeat('X', 5):")
    for x in itertools.repeat("X", 5):
        print(x, end=" ")
    print()

    # CHAIN
    separator("CHAIN")

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7]

    chained = itertools.chain(list1, list2, list3)
    print("chain:", list(chained))

    # ISLICE
    separator("ISLICE")

    data = range(100)
    sliced = itertools.islice(data, 10, 20, 2)
    print("islice(range(100), 10, 20, 2):", list(sliced))

    # ACCUMULATE
    separator("ACCUMULATE")

    numbers = [1, 2, 3, 4, 5]

    print("accumulate (sum):", list(itertools.accumulate(numbers)))
    print("accumulate (product):",
          list(itertools.accumulate(numbers, operator.mul)))

    # COMBINATORICS
    separator("COMBINATORICS")

    items = ["A", "B", "C"]

    print("product (cartesian product):")
    print(list(itertools.product(items, repeat=2)))

    print("\npermutations (order matters):")
    print(list(itertools.permutations(items, 2)))

    print("\ncombinations (order does NOT matter):")
    print(list(itertools.combinations(items, 2)))

    print("\ncombinations_with_replacement:")
    print(list(itertools.combinations_with_replacement(items, 2)))

    # GROUPBY
    separator("GROUPBY")

    data = [
        {"name": "Alice", "dept": "IT"},
        {"name": "Bob", "dept": "IT"},
        {"name": "Carol", "dept": "HR"},
        {"name": "Dave", "dept": "HR"},
        {"name": "Eve", "dept": "Sales"},
    ]

    # IMPORTANT: groupby requires sorted data
    data.sort(key=lambda x: x["dept"])

    for dept, group in itertools.groupby(data, key=lambda x: x["dept"]):
        print(dept, "->", list(group))

    # REAL-WORLD PIPELINE EXAMPLE
    separator("REAL-WORLD PIPELINE")

    # Simulate a stream of events
    events = [
        ("login", "alice"),
        ("login", "bob"),
        ("logout", "alice"),
        ("login", "alice"),
        ("logout", "bob"),
    ]

    # Count consecutive event types
    for event_type, group in itertools.groupby(events, key=lambda x: x[0]):
        count = sum(1 for _ in group)
        print(event_type, "occurred", count, "times consecutively")

if __name__ == "__main__":
    main()
