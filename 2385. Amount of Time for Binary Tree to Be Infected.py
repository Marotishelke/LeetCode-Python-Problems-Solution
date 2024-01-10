# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        result = 0

        def dfs(node, first):
            if node == None:
                return 0
            
            # Visiting all the nodes of Left sub tree 
            left_depth = dfs(node.left, first)

            # Visiting all the nodes of Right sub tree
            right_depth = dfs(node.right, first)

            if node.val == first:
                Solution.result = max(left_depth, right_depth)
                return -1
            
            elif left_depth >= 0 and right_depth >= 0:
                return max(left_depth, right_depth) + 1
            
            Solution.result = max(Solution.result, abs(left_depth - right_depth))
            return min(left_depth, right_depth) - 1

        dfs(root, start)
        return Solution.result
