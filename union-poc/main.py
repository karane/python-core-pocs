from typing import Union

def parse_input(value: Union[int, float, str]) -> float:
    """
    Accepts int, float, or str.
    Returns a float version of the input.
    Shows how to detect the real type at runtime.
    """
    print(f"Received value: {value} (type={type(value).__name__})")

    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):
        # Try converting string to float
        try:
            return float(value.strip())
        except ValueError:
            raise ValueError(f"String '{value}' cannot be converted to float")

    # This should never happen due to Union typing
    raise TypeError("Unsupported type")


# Union as a return type
def safe_div(a: float, b: float) -> Union[float, str]:
    """
    Returns either:
    - a float (division result)
    - a string error message
    """
    if b == 0:
        return "Error: division by zero"
    return a / b


def main():
    print("---- Testing parse_input ----")
    print(parse_input(10))        # int
    print(parse_input(3.14))      # float
    print(parse_input("  5.55 ")) # str

    print("\n---- Testing safe_div ----")
    print(safe_div(10, 2))   # returns float
    print(safe_div(10, 0))   # returns string


if __name__ == "__main__":
    main()
