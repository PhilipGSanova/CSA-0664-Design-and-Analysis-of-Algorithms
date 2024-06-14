def most_profitable_path(edges, bob, amount):
    from collections import defaultdict, deque
    
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def find_bob_path(node, parent):
        if node == 0:
            return [node]
        for neighbor in tree[node]:
            if neighbor != parent:
                path = find_bob_path(neighbor, node)
                if path:
                    return path + [node]
        return []
    
    bob_path = find_bob_path(bob, -1)
    bob_time = {node: time for time, node in enumerate(bob_path)}
    
    def dfs(node, parent, time):
        profit = amount[node]
        if node in bob_time:
            if bob_time[node] < time:
                profit = 0
            elif bob_time[node] == time:
                profit //= 2
        
        max_profit = float('-inf')
        is_leaf = True
        
        for neighbor in tree[node]:
            if neighbor != parent:
                is_leaf = False
                max_profit = max(max_profit, dfs(neighbor, node, time + 1))
        
        if is_leaf:
            return profit
        
        return profit + max_profit
    
    return dfs(0, -1, 0)

edges1 = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob1 = 3
amount1 = [-2, 4, 2, -4, 6]
print(most_profitable_path(edges1, bob1, amount1))