class DynamicObject:
    def __init__(self):
        # Normal attribute
        self.name = "Karane"

    def __getattr__(self, attr):
        print(f"[__getattr__] Attribute '{attr}' not found. Returning a dynamic value.")
        return f"<dynamic value for '{attr}'>"

    def __setattr__(self, attr, value):
        print(f"[__setattr__] Setting '{attr}' to '{value}'")
        super().__setattr__(attr, value)


def main():
    obj = DynamicObject()

    # Reading existing attribute
    print("\n1) Reading existing attribute:")
    print(obj.name)  # normal

    # Setting new dynamic attribute
    print("\n2) Setting new dynamic attribute:")
    setattr(obj, "age", 42)
    print(obj.age)

    # Checking attribute existence
    print("\n3) Checking attributes:")
    print("Has 'name'?  ", hasattr(obj, "name"))
    print("Has 'foo'?   ", hasattr(obj, "foo"))

    # Using getattr with default
    print("\n4) getattr with default:")
    print(getattr(obj, "country", "Brazil"))

    # Triggering __getattr__
    print("\n5) Accessing missing attribute:")
    print(obj.favorite_color)  # triggers __getattr__


if __name__ == "__main__":
    main()
