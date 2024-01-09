# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def tree(root, leafNodeTree):
            if root:
                #base condition 
                if not root.left and not root.right:
                    leafNodeTree.append(root.val)
                tree(root.left, leafNodeTree)
                tree(root.right, leafNodeTree)
                return leafNodeTree
            
        return tree(root1, []) == tree(root2, [])
        
