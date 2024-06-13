from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minSwapsToSort(arr):
    n = len(arr)
    arr_pos = list(enumerate(arr))
    arr_pos.sort(key=lambda it: it[1])
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or arr_pos[i][0] == i:
            continue

        cycle_size = 0
        x = i
        while not visited[x]:
            visited[x] = True
            x = arr_pos[x][0]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps

def minOperationsToSortTree(root):
    if not root:
        return 0
    
    queue = deque([root])
    operations = 0
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        operations += minSwapsToSort(level_values)
    
    return operations

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(5)
root.left.left.left = None
root.left.left.right = None
root.left.right.left = None
root.left.right.right = None
root.right.left.left = TreeNode(9)
root.right.left.right = None
root.right.right.left = TreeNode(10)
root.right.right.right = None

print(minOperationsToSortTree(root)) 