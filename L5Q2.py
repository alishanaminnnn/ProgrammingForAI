def distance(x1, y1, x2=0, y2=0):
    # Calculate the distance between two points
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d

# Distance from (3, 4) to the origin (0, 0)
print("Distance 1: ", distance(3, 4))

# Distance between points (1, 2) and (4, 6)
print("Distance 2: ", distance(1, 2, 4, 6))
