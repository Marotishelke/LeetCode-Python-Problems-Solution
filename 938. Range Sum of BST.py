# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.Sum = 0
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        self.rangeSumBST(root.left, low, high)
        rootValue = root.val
        if rootValue <= high and rootValue >= low:
            self.Sum += rootValue
        self.rangeSumBST(root.right, low, high)
        return self.Sum
