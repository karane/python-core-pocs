
# 1. Custom Iterator Class

class CountDown:
    """Custom iterator that counts down from a given number to 1."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Iterator must return itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num



# 2. Generator Function

def countdown(n):
    """A generator function that yields numbers from n down to 1."""
    while n > 0:
        yield n  # yield pauses execution and remembers state
        n -= 1



# 3. Generator Expression

def square_generator(limit):
    """Returns a generator expression that lazily computes squares."""
    return (x * x for x in range(limit))



# 4. Infinite Generator

def infinite_even_numbers():
    """Infinite generator that yields even numbers."""
    n = 0
    while True:
        yield n
        n += 2



# Demo Section

if __name__ == "__main__":
    print("=== 1. Custom Iterator Class ===")
    countdown_iter = CountDown(5)
    for number in countdown_iter:
        print(number, end=" ")
    print("\n")

    print("=== 2. Generator Function ===")
    for number in countdown(5):
        print(number, end=" ")
    print("\n")

    print("=== 3. Generator Expression ===")
    squares = square_generator(5)
    for s in squares:
        print(s, end=" ")
    print("\n")

    print("=== 4. Infinite Generator (first 5 even numbers) ===")
    evens = infinite_even_numbers()
    for _ in range(5):
        print(next(evens), end=" ")
    print("\n")

    print("All done!")
