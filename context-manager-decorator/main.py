import time
from contextlib import contextmanager

@contextmanager
def log_context(name):
    print(f"[ENTER] Starting {name}...")
    start_time = time.time()
    try:
        # This is equivalent to __enter__()
        yield  # control passes to the with-block here
    except Exception as e:
        # This is where you can handle exceptions
        print(f"[ERROR] {name}: {type(e).__name__} - {e}")
        raise  # re-raise exception after logging
    finally:
        # This is equivalent to __exit__()
        end_time = time.time()
        print(f"[EXIT] Finished {name} in {end_time - start_time:.2f}s")


def slow_function():
    time.sleep(1)
    print("Doing work...")


def failing_function():
    time.sleep(0.5)
    raise ValueError("Simulated error")


if __name__ == "__main__":
    print("=== Normal Execution ===")
    with log_context("slow_function"):
        slow_function()

    print("\n=== With Exception ===")
    try:
        with log_context("failing_function"):
            failing_function()
    except ValueError:
        print("Caught exception outside context")
