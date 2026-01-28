import time

class LogContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"[ENTER] Starting {self.name}...")
        self.start_time = time.time()
        # Return something useful if needed
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"[EXIT] Finished {self.name} in {end_time - self.start_time:.2f}s")

        # Handle exceptions if any
        if exc_type:
            print(f"[ERROR] {exc_type.__name__}: {exc_value}")
            # Returning True suppresses the exception
            return False  # re-raise the exception

# Example usage
def slow_function():
    time.sleep(1)
    print("Doing work...")

if __name__ == "__main__":
    print("=== Normal Execution ===")
    with LogContext("slow_function"):
        slow_function()

    print("\n=== With Exception ===")
    try:
        with LogContext("failing_function"):
            raise RuntimeError("Simulated failure")
    except RuntimeError:
        print("Caught exception outside context")
