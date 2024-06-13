import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_dist, node = heapq.heappop(priority_queue)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return dist

def minCostToBuyApples(n, roads, appleCost, k):
    graph = [[] for _ in range(n + 1)]
    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    shortest_paths = []
    for i in range(1, n + 1):
        shortest_paths.append(dijkstra(n, graph, i))
    
    answer = []
    for i in range(1, n + 1):
        min_cost = float('inf')
        for j in range(1, n + 1):
            if i == j:
                min_cost = min(min_cost, appleCost[j - 1])
            else:
                to_j_cost = shortest_paths[i - 1][j]
                from_j_cost = shortest_paths[j - 1][i] * k
                total_cost = to_j_cost + appleCost[j - 1] + from_j_cost
                min_cost = min(min_cost, total_cost)
        answer.append(min_cost)
    
    return answer

n1 = 4
roads1 = [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]]
appleCost1 = [56, 42, 102, 301]
k1 = 2
print(minCostToBuyApples(n1, roads1, appleCost1, k1))

n2 = 3
roads2 = [[1, 2, 5], [2, 3, 1], [3, 1, 2]]
appleCost2 = [2, 3, 1]
k2 = 3
print(minCostToBuyApples(n2, roads2, appleCost2, k2))