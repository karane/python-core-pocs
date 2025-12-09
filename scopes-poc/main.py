# Global variable
counter = 0

def outer():
    # Enclosing scope
    message = "Outer says hi"

    def inner():
        # Local scope
        nonlocal message   # Refers to the variable in the enclosing (outer) scope
        global counter     # Refers to the global variable at the top level

        message = "Inner changed this message"
        counter += 1  # Modify the global variable

        print("Inside inner():")
        print("  message =", message)
        print("  counter =", counter)

    inner()

    print("Inside outer() after inner() call:")
    print("  message =", message)
    print("  counter =", counter)


def main():
    print("Before any call:")
    print("  counter =", counter)
    print()

    outer()
    print()
    print("After outer() call:")
    print("  counter =", counter)


if __name__ == "__main__":
    main()
