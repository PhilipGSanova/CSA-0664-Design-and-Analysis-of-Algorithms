import numpy as np

def travelling_salesman(graph):
    n = len(graph)
    all_points = frozenset(range(n))
    memo = {}

    def tsp_dp(curr, remaining):
        if not remaining:
            return graph[curr][0]
        
        if (curr, remaining) in memo:
            return memo[(curr, remaining)]
        
        res = min([graph[curr][next] + tsp_dp(next, remaining - frozenset([next])) for next in remaining])
        memo[(curr, remaining)] = res
        return res

    return tsp_dp(0, all_points - frozenset([0]))

graph = np.array([[0, 10, 15, 20],
                  [5, 0, 9, 10],
                  [6, 13, 0, 12],
                  [8, 8, 9, 0]])
print(travelling_salesman(graph))
