from functools import reduce


def separator(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


def main():
    numbers = [1, 2, 3, 4, 5, 6]

    separator("ORIGINAL DATA")
    print("numbers =", numbers)

    # MAP
    separator("MAP - Transform each element")

    # Square each number
    squared = list(map(lambda x: x * x, numbers))
    print("Squared:", squared)

    # Equivalent list comprehension
    squared_lc = [x * x for x in numbers]
    print("Squared (list comprehension):", squared_lc)


    # FILTER
    separator("FILTER - Select elements")

    # Keep only even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", evens)

    # Equivalent list comprehension
    evens_lc = [x for x in numbers if x % 2 == 0]
    print("Even numbers (list comprehension):", evens_lc)

    # REDUCE
    separator("REDUCE - Combine elements")

    # Sum all numbers
    total = reduce(lambda acc, x: acc + x, numbers)
    print("Sum:", total)

    # Multiply all numbers
    product = reduce(lambda acc, x: acc * x, numbers)
    print("Product:", product)

    # MAP + FILTER + REDUCE COMBINED
    separator("MAP + FILTER + REDUCE")

    result = reduce(
        lambda acc, x: acc + x,
        filter(
            lambda x: x > 10,
            map(lambda x: x * x, numbers)
        ),
        0
    )

    print("Result (squares > 10, summed):", result)

    # Step-by-step equivalent
    squared = map(lambda x: x * x, numbers)
    filtered = filter(lambda x: x > 10, squared)
    result_step_by_step = reduce(lambda acc, x: acc + x, filtered, 0)

    print("Result (step by step):", result_step_by_step)

    # REAL-WORLD EXAMPLE
    separator("REAL-WORLD EXAMPLE")

    orders = [
        {"item": "Book", "price": 30, "paid": True},
        {"item": "Pen", "price": 5, "paid": False},
        {"item": "Laptop", "price": 3000, "paid": True},
    ]

    print("Orders:", orders)

    # Total price of paid orders
    total_paid = reduce(
        lambda acc, price: acc + price,
        map(
            lambda o: o["price"],
            filter(lambda o: o["paid"], orders)
        ),
        0
    )

    print("Total paid:", total_paid)

    # PYTHONIC ALTERNATIVE
    separator("PYTHONIC ALTERNATIVE")

    total_paid_pythonic = sum(o["price"] for o in orders if o["paid"])
    print("Total paid (pythonic):", total_paid_pythonic)

if __name__ == "__main__":
    main()
