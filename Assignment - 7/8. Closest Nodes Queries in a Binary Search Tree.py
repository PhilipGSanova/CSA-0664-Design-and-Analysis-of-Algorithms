from bisect import bisect_left, bisect_right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def closest_nodes(root, queries):
    sorted_vals = inorder_traversal(root)
    result = []

    for q in queries:
        pos_left = bisect_right(sorted_vals, q) - 1
        pos_right = bisect_left(sorted_vals, q)

        mini = sorted_vals[pos_left] if pos_left >= 0 else -1
        maxi = sorted_vals[pos_right] if pos_right < len(sorted_vals) else -1
        
        result.append([mini, maxi])
    
    return result

root = TreeNode(6,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(4)),
                TreeNode(13,
                         TreeNode(9),
                         TreeNode(15,
                                  TreeNode(14))))

queries = [2, 5, 16]
print(closest_nodes(root, queries)) 