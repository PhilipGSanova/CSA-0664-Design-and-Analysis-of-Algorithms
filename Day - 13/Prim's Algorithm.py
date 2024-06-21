import sys

def prim(graph):

    num_vertices = len(graph)
    selected = [False] * num_vertices
    no_edge = 0
    selected[0] = True
    mst_edges = []
    total_cost = 0

    print("Edge : Weight")
    while no_edge < num_vertices - 1:
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if (not selected[j]) and graph[i][j]:  # not in selected and there is an edge
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x}-{y}: {graph[x][y]}")
        mst_edges.append((x, y, graph[x][y]))
        total_cost += graph[x][y]
        selected[y] = True
        no_edge += 1

    return mst_edges, total_cost

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst_edges, total_cost = prim(graph)
print("\nEdges in MST:", mst_edges)
print("Total cost of MST:", total_cost)
