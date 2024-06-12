def closest_pair(points):
    def euclidean_distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

    def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
        n = len(points_sorted_by_x)
        
        if n <= 3:
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, euclidean_distance(points_sorted_by_x[i], points_sorted_by_x[j]))
            return min_dist

        mid = n // 2
        midpoint = points_sorted_by_x[mid]

        left_half_x = points_sorted_by_x[:mid]
        right_half_x = points_sorted_by_x[mid:]
        
        left_half_y = list(filter(lambda p: p[0] <= midpoint[0], points_sorted_by_y))
        right_half_y = list(filter(lambda p: p[0] > midpoint[0], points_sorted_by_y))

        d1 = closest_pair_recursive(left_half_x, left_half_y)
        d2 = closest_pair_recursive(right_half_x, right_half_y)
        d = min(d1, d2)

        strip = [p for p in points_sorted_by_y if abs(p[0] - midpoint[0]) < d]

        strip_len = len(strip)
        for i in range(strip_len):
            for j in range(i + 1, min(i + 7, strip_len)): 
                d = min(d, euclidean_distance(strip[i], strip[j]))

        return d

    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])

    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("The smallest distance is", closest_pair(points))