import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Initialize the distances to all nodes as infinity and the distance to the start node as 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue to hold nodes to visit
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Nodes can be added multiple times to the priority queue; we only process the first time we remove it
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# You can give the input as a graph here
graph = {
    1: {2: 7, 3: 9, 6: 14},
    2: {1: 7, 3: 10, 4: 15},
    3: {1: 9, 2: 10, 4: 11, 6: 2},
    4: {2: 15, 3: 11, 5: 6},
    5: {4: 6, 6: 9},
    6: {1: 14, 3: 2, 5: 9}
}

# Run Dijkstra's algorithm from node 1
start_node = 1
distances = dijkstra(graph, start_node)

# Print the results
print("Shortest distances from node", start_node, ":", distances)

# Create a directed graph for visualization
G = nx.DiGraph()

# Add nodes (intersections)
G.add_nodes_from(graph.keys())

# Add edges (roads) with weights (travel times)
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Position nodes using a layout
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight the shortest paths from the start node
shortest_path_edges = [(start_node, neighbor) for neighbor in graph[start_node]]

# Draw the shortest paths in a different color
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=2)

# Display the shortest path distances on the nodes
node_labels = {node: f"{node}\n{distances[node]:.2f}" for node in distances}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='black')

# Show the plot
plt.title(f"Shortest Paths from Node {start_node}")
plt.show()
