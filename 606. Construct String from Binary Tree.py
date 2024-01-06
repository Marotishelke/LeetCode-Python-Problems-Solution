# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:  
        res = []
        self.dfs(root, res)
        return ''.join(res)

    def dfs(self, t, res):
        if t is None:
            return

        res.append(str(t.val))

        if t.left is None and t.right is None:
            return

        res.append('(')
        self.dfs(t.left, res)
        res.append(')')

        if t.right is not None:
            res.append('(')
            self.dfs(t.right, res)
            res.append(')')
