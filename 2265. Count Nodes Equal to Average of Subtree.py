# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # ---------------------------------------
    # Approach 1
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node):
            nonlocal result

            if not node:
                return 0, 0
            
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            if curr_sum // curr_count == node.val:
                result += 1
            
            return curr_sum, curr_count
        
        traverse(root)
        return result
    # ---------------------------------------

    # ---------------------------------------
    # Approach 2
    def __init__(self):
        self.result = 0
        
    def averageOfSubtree(self, root):
        self.dfs(root)
        return self.result
        
    def dfs(self, node):
        if not node:
            return [0, 0]
            
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        currentSum = left[0] + right[0] + node.val
        currentCount = left[1] + right[1] + 1

        if currentSum // currentCount == node.val:
            self.result += 1
            
        return [currentSum, currentCount]
    # ---------------------------------------
        
