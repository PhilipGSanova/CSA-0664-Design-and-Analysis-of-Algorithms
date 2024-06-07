import numpy as np

def travelling_salesman_problem(distances):
    n = len(distances)
    all_points_set = set(range(n))
    memo = {}

    def tsp_dp(start, points):
        if (start, points) in memo:
            return memo[(start, points)]

        if not points:
            return distances[start][0]

        min_cost = min([distances[start][point] + tsp_dp(point, points - {point}) for point in points])

        memo[(start, points)] = min_cost
        return min_cost

    return tsp_dp(0, all_points_set - {0})

# Example usage
distances = np.array([[0, 10, 15, 20],
                       [10, 0, 35, 25],
                       [15, 35, 0, 30],
                       [20, 25, 30, 0]])

print(travelling_salesman_problem(distances))
