import time
import random

# 1. Basic decorator: logging
def log_call(func):
    """Decorator that logs function calls and execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[LOG] {func.__name__} returned {result} (took {duration:.4f}s)\n")
        return result
    return wrapper


# 2. Decorator with arguments: retry
def retry(times=3, delay=1):
    """Decorator that retries a function if it raises an exception."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    print(f"[RETRY] Attempt {attempt} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[ERROR] {e}")
                    if attempt < times:
                        print(f"Retrying in {delay} second(s)...\n")
                        time.sleep(delay)
                    else:
                        print(f"[FAILED] {func.__name__} failed after {times} attempts\n")
                        raise
        return wrapper
    return decorator


# 3. Example functions using decorators
@log_call
def greet(name="world"):
    """Simple greeting."""
    time.sleep(0.3)
    return f"Hello, {name}!"


@log_call
@retry(times=3, delay=1)
def unstable_task():
    """Simulate an unreliable function that sometimes fails."""
    time.sleep(0.2)
    if random.random() < 0.5:
        raise ValueError("Something went wrong!")
    return "Success!"


def main():
    print("=== Decorators Demo ===\n")
    greet("Alice")
    print("-" * 40)
    try:
        unstable_task()
    except Exception:
        print("Task ultimately failed after retries.\n")


if __name__ == "__main__":
    main()
