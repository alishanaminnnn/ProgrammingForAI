import math

def is_triangle(a, b, c):
    # Check the triangle inequality
    return a + b > c and a + c > b and b + c > a


def triangle_area(a, b, c):
    """Return the area if valid, otherwise return 0."""
    if not is_triangle(a, b, c):
        return 0

    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Apply Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


# Test both triangles
print("Area of triangle (3, 4, 5):", triangle_area(3, 4, 5))
print("Area of triangle (1, 2,3):", triangle_area(1, 2, 3))
