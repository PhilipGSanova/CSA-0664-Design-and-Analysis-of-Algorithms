def convex_hull(points):
    # Function to determine if the sequence of three points makes a counter-clockwise turn
    def ccw(p1, p2, p3):
        return (p2[1] - p1[1]) * (p3[0] - p2[0]) > (p2[0] - p1[0]) * (p3[1] - p2[1])

    # Sort points lexicographically (tuples are compared lexicographically by default)
    points = sorted(points)

    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and not ccw(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and not ccw(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)

    # Remove the last point of each half because it is repeated at the beginning of the other half
    return lower[:-1] + upper[:-1]

# Example usage:
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = convex_hull(points)
print("The points in the convex hull are:", hull)
