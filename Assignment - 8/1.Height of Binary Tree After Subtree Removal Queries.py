class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height_of_tree(node):
    if not node:
        return -1
    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)
    return 1 + max(left_height, right_height)

def build_tree_from_list(vals):
    if not vals:
        return None
    nodes = [None if val is None else TreeNode(val) for val in vals]
    kid_idx = 1
    for idx, node in enumerate(nodes):
        if node is not None:
            if kid_idx < len(nodes) and nodes[kid_idx] is not None:
                node.left = nodes[kid_idx]
            kid_idx += 1
            if kid_idx < len(nodes) and nodes[kid_idx] is not None:
                node.right = nodes[kid_idx]
            kid_idx += 1
    return nodes[0]

def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left_result = find_node(root.left, val)
    if left_result is not None:
        return left_result
    return find_node(root.right, val)

def height_after_removal(root, query):
    target_node = find_node(root, query)
    if not target_node:
        return height_of_tree(root)
    if target_node.left:
        original_left = target_node.left
        target_node.left = None
        height_with_left_removed = height_of_tree(root)
        target_node.left = original_left
        return height_with_left_removed
    if target_node.right:
        original_right = target_node.right
        target_node.right = None
        height_with_right_removed = height_of_tree(root)
        target_node.right = original_right
        return height_with_right_removed
    return height_of_tree(root)

def height_after_subtree_removal(root, queries):
    root_tree_height = height_of_tree(root)
    results = []
    for query in queries:
        results.append(height_after_removal(root, query))
    return results

root_vals = [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7]
queries = [4]
root = build_tree_from_list(root_vals)
print(height_after_subtree_removal(root, queries))