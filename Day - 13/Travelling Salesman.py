import numpy as np
def travellingsalesman(graph):
    n=len(graph)
    all_points=frozenset(range(n))
    memo={}

    def tsp_dp(start,points):
        if (start,points) in memo:
            return memo[(start,points)]
        
        if not points:
            return graph[start][0]
        
        min_cost=min([graph[start][point]+tsp_dp(point,all_points-frozenset([0])) for point in points])
        memo[(start,points)] = min_cost
        return min_cost
    return tsp_dp(0,all_points-frozenset([0]))

graph = np.array([[0,5,7,np.inf,2],
                  [5,0,np.inf,6,3],
                  [7,np.inf,0,4,4],
                  [np.inf,6,4,5,0],
                  [2,3,4,5,0]])
print(travellingsalesman(graph))
