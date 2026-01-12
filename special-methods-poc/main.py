class Vector:
    def __init__(self, *values):
        """Initialize with any number of numeric values."""
        self._values = list(values)

    # String representations
    def __str__(self):
        return f"Vector{tuple(self._values)}"

    def __repr__(self):
        return f"Vector({', '.join(str(v) for v in self._values)})"

    # Length and iteration
    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        self._values[index] = value

    def __delitem__(self, index):
        del self._values[index]

    def __iter__(self):
        return iter(self._values)

    # Comparison
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self._values == other._values

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return sum(self._values) < sum(other._values)

    # Arithmetic operations
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError("Vectors must be the same length")
        return Vector(*(a + b for a, b in zip(self._values, other._values)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError("Vectors must be the same length")
        return Vector(*(a - b for a, b in zip(self._values, other._values)))

    def __mul__(self, scalar):
        return Vector(*(a * scalar for a in self._values))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Utility methods
    def __contains__(self, item):
        return item in self._values

    def __bool__(self):
        """Vectors are False if empty or all values are zero."""
        return any(self._values)

    def __abs__(self):
        """Return magnitude (Euclidean norm)."""
        return sum(a ** 2 for a in self._values) ** 0.5


# --- Example usage ---
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(1, 2, 3)

print("String:", v1)
print("Repr:", repr(v1))
print("Length:", len(v1))
print("Indexing:", v1[0])
print("Iteration:", [x for x in v1])

print("Equality:", v1 == v3)
print("Less than:", v1 < v2)
print("Addition:", v1 + v2)
print("Subtraction:", v2 - v1)
print("Scalar multiplication:", v1 * 3)
print("Reverse multiplication:", 3 * v1)
print("Contains 2?", 2 in v1)
print("Magnitude:", abs(v1))

v1[0] = 10
print("Modified:", v1)
del v1[1]
print("After deletion:", v1)
print("Boolean value:", bool(v1))
