def discriminant(a, b, c):
    """Calculate and return the discriminant of a quadratic equation."""
    D = (b**2) - (4*a*c)
    return D


def quadratic_roots(a, b, c):
    """Calculate the real roots using the discriminant."""
    D = discriminant(a, b, c)

    if D > 0:
        # Calculate two distinct real roots
        negative = (-b - (D**0.5)) / (2*a)
        positive = (-b + (D**0.5)) / (2*a)
        return positive, negative

    elif D == 0:
        # Calculate the single repeated root
        root = -b / (2*a)
        return root

    else:
        # No real roots exist
        return "No real Roots"


# Test the function with a = 1, b = -5, c = 6
a = 1
b = -5
c = 6

result = quadratic_roots(a, b, c)
print(result)

# Display the function's documentation
print(quadratic_roots.__doc__:)
