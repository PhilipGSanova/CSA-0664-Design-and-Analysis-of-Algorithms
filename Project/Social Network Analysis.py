import numpy as np

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
    graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C']
    }
    
    scores = pagerank(graph)
    
    for node, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"Node {node}: PageRank score = {score:.4f}")
