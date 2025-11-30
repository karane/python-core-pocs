def make_greeter(name):
    """Return a greeter function that remembers the given name."""
    count = 0  # This variable is enclosed (captured) by the inner function

    def greeter():
        nonlocal count  # allows modification of the enclosed variable
        count += 1
        print(f"Hi, I'm {name}! (I've greeted you {count} time(s))")

    return greeter


def main():
    # Create independent greeters
    alice_greeter = make_greeter("Alice")
    bob_greeter = make_greeter("Bob")

    # Each greeter has its own enclosed "count" variable
    alice_greeter()  
    alice_greeter()  
    bob_greeter()    
    alice_greeter()  
    bob_greeter()   


if __name__ == "__main__":
    main()
