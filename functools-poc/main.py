from functools import partial, lru_cache
import time


def separator(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


# PARTIAL
def multiply(a, b):
    return a * b


# LRU CACHE
def slow_fibonacci(n):
    """Intentionally slow Fibonacci (no cache)."""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


@lru_cache(maxsize=128)
def fast_fibonacci(n):
    """Fast Fibonacci using lru_cache."""
    if n <= 1:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)


def main():
    separator("functools.partial")

    # Create a new function by fixing some arguments
    double = partial(multiply, 2)
    triple = partial(multiply, 3)

    print("double(10) =", double(10))
    print("triple(10) =", triple(10))

    # Partial with keyword arguments
    def power(base, exponent):
        return base ** exponent

    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)

    print("square(5) =", square(5))
    print("cube(5) =", cube(5))

    # Partial is useful when passing callbacks
    numbers = [1, 2, 3, 4]

    doubled_numbers = list(map(double, numbers))
    print("Doubled list:", doubled_numbers)

    separator("functools.lru_cache")

    n = 35

    print(f"Calculating fibonacci({n}) without cache...")
    start = time.time()
    result_slow = slow_fibonacci(n)
    end = time.time()
    print("Result:", result_slow)
    print("Time (slow):", round(end - start, 2), "seconds")

    print(f"\nCalculating fibonacci({n}) with lru_cache...")
    start = time.time()
    result_fast = fast_fibonacci(n)
    end = time.time()
    print("Result:", result_fast)
    print("Time (cached):", round(end - start, 2), "seconds")

    # Cache info
    print("\nCache info:", fast_fibonacci.cache_info())

    # Clear cache
    fast_fibonacci.cache_clear()
    print("Cache cleared.")
    print("Cache info after clear:", fast_fibonacci.cache_info())

    separator("LRU CACHE - PRACTICAL USE")

    @lru_cache(maxsize=4)
    def fetch_user(user_id):
        print(f"Fetching user {user_id} from database...")
        time.sleep(1)  # simulate slow I/O
        return {"id": user_id, "name": f"User-{user_id}"}

    print(fetch_user(1))
    print(fetch_user(2))
    print(fetch_user(1))  # cached
    print(fetch_user(3))
    print(fetch_user(4))
    print(fetch_user(5))  # causes eviction (maxsize=4)

    print("\nCache info:", fetch_user.cache_info())


if __name__ == "__main__":
    main()
