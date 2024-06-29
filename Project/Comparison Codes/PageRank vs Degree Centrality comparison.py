import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def pagerank(graph, damping_factor=0.85, max_iterations=100, tolerance=1.0e-6):
    """
    Calculate PageRank scores for nodes in a graph represented as adjacency lists.
    
    Parameters:
    - graph: Dictionary where keys are nodes and values are lists of nodes representing outgoing edges.
    - damping_factor: Probability of following a link (typically set to 0.85).
    - max_iterations: Maximum number of iterations for convergence.
    - tolerance: Convergence threshold.
    
    Returns:
    - pagerank_scores: Dictionary where keys are nodes and values are their PageRank scores.
    """
    num_nodes = len(graph)
    initial_score = 1.0 / num_nodes
    pagerank_scores = {node: initial_score for node in graph}
    converged = False
    iteration = 0
    
    while not converged and iteration < max_iterations:
        iteration += 1
        new_pagerank_scores = {}
        sink_pr = 0
        
        for node in graph:
            if len(graph[node]) == 0:
                sink_pr += pagerank_scores[node]
        
        for node in graph:
            new_pagerank_score = (1.0 - damping_factor) / num_nodes
            new_pagerank_score += damping_factor * sink_pr / num_nodes
            
            for neighbor in graph[node]:
                new_pagerank_score += damping_factor * pagerank_scores[neighbor] / len(graph[neighbor])
            
            new_pagerank_scores[node] = new_pagerank_score
        
        # Check convergence using L1 norm
        delta = sum(abs(new_pagerank_scores[node] - pagerank_scores[node]) for node in graph)
        converged = delta < tolerance
        pagerank_scores = new_pagerank_scores
    
    return pagerank_scores

if __name__ == "__main__":
    # Create a graph
    G = nx.karate_club_graph()

    # Convert networkx graph to adjacency list format for custom PageRank
    graph = {node: list(G.neighbors(node)) for node in G.nodes()}

    # Compute custom PageRank
    custom_page_rank = pagerank(graph)

    # Compute built-in PageRank for comparison
    nx_page_rank = nx.pagerank(G)

    # Compute Degree Centrality
    degree_centrality = nx.degree_centrality(G)

    # Sort nodes by PageRank and Degree Centrality for comparison
    sorted_custom_page_rank = sorted(custom_page_rank.items(), key=lambda x: x[1], reverse=True)
    sorted_nx_page_rank = sorted(nx_page_rank.items(), key=lambda x: x[1], reverse=True)
    sorted_degree_centrality = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

    # Extract node labels and corresponding centrality values
    nodes_custom_page_rank, custom_pr_values = zip(*sorted_custom_page_rank)
    nodes_nx_page_rank, nx_pr_values = zip(*sorted_nx_page_rank)
    nodes_degree_centrality, dc_values = zip(*sorted_degree_centrality)

    # Convert nodes to strings for better plotting
    nodes_custom_page_rank = [str(node) for node in nodes_custom_page_rank]
    nodes_nx_page_rank = [str(node) for node in nodes_nx_page_rank]
    nodes_degree_centrality = [str(node) for node in nodes_degree_centrality]

    # Plot custom PageRank vs Degree Centrality
    plt.figure(figsize=(15, 8))

    plt.subplot(1, 2, 1)
    plt.bar(nodes_custom_page_rank, custom_pr_values, color='b')
    plt.xticks(rotation=90)
    plt.xlabel('Nodes')
    plt.ylabel('Custom PageRank')
    plt.title('Custom PageRank of Nodes')

    plt.subplot(1, 2, 2)
    plt.bar(nodes_degree_centrality, dc_values, color='r')
    plt.xticks(rotation=90)
    plt.xlabel('Nodes')
    plt.ylabel('Degree Centrality')
    plt.title('Degree Centrality of Nodes')

    plt.tight_layout()
    plt.show()

    # Comparison plot to show the difference
    # Normalize the values for better comparison
    custom_pr_values = np.array(custom_pr_values)
    dc_values = np.array(dc_values)
    custom_pr_values_norm = (custom_pr_values - custom_pr_values.min()) / (custom_pr_values.max() - custom_pr_values.min())
    dc_values_norm = (dc_values - dc_values.min()) / (dc_values.max() - dc_values.min())

    plt.figure(figsize=(10, 6))

    plt.plot(nodes_custom_page_rank, custom_pr_values_norm, marker='o', linestyle='-', color='b', label='Normalized Custom PageRank')
    plt.plot(nodes_degree_centrality, dc_values_norm, marker='s', linestyle='--', color='r', label='Normalized Degree Centrality')

    plt.xticks(rotation=90)
    plt.xlabel('Nodes')
    plt.ylabel('Normalized Centrality Values')
    plt.title('Comparison of Custom PageRank and Degree Centrality')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
