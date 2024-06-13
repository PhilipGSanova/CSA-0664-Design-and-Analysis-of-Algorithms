from collections import defaultdict
import math

def minimumFuelCost(roads, seats):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent):
        total_reps = 1
        total_fuel = 0
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            reps_from_subtree, fuel_from_subtree = dfs(neighbor, node)
            total_reps += reps_from_subtree
            total_fuel += fuel_from_subtree
        
        if node != 0:
            trips = math.ceil(total_reps / seats)
            total_fuel += trips
        return total_reps, total_fuel

    _, total_fuel = dfs(0, -1)
    return total_fuel

roads1 = [[0, 1], [0, 2], [0, 3]]
seats1 = 5
print(minimumFuelCost(roads1, seats1))

roads2 = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats2 = 2
print(minimumFuelCost(roads2, seats2))

roads3 = []
seats3 = 1
print(minimumFuelCost(roads3, seats3))
