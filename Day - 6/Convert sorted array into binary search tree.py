class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root

# Example 1
nums1 = [-10, -3, 0, 5, 9]
root1 = sortedArrayToBST(nums1)

# Example 2
nums2 = [1, 3]
root2 = sortedArrayToBST(nums2)
