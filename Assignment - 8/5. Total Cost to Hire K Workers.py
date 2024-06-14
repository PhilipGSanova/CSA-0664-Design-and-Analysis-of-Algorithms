from heapq import heappop, heappush

def total_cost_to_hire_workers(costs, k, candidates):
    n = len(costs)
    
    left_heap = []
    right_heap = []
    
    for i in range(min(candidates, n)):
        heappush(left_heap, (costs[i], i))
    
    for i in range(max(candidates, n - candidates), n):
        heappush(right_heap, (costs[i], i))
    
    total_cost = 0
    hired_count = 0
    left_index = min(candidates, n)
    right_index = max(candidates, n - candidates)
    
    while hired_count < k:
        if left_heap and (not right_heap or left_heap[0][0] <= right_heap[0][0]):
            cost, index = heappop(left_heap)
            total_cost += cost
            if left_index < right_index:
                heappush(left_heap, (costs[left_index], left_index))
                left_index += 1
        else:
            cost, index = heappop(right_heap)
            total_cost += cost
            if right_index > left_index:
                heappush(right_heap, (costs[right_index - 1], right_index - 1))
                right_index -= 1
        
        hired_count += 1
    
    return total_cost

costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
print(total_cost_to_hire_workers(costs, k, candidates)) 