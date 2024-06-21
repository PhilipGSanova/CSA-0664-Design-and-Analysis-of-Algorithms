def warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
    return graph

# Example graph
graph = [[0, 1, 0],
         [0, 0, 1],
         [1, 0, 0]]

result = warshall(graph)
for row in result:
    print(row)
