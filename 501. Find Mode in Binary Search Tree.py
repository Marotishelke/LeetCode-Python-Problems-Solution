# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        # -----------------------------------
        # Approach 1
        """
            Store all the elements in lst from tree.
            Then find the frequency of each element.
            Find often element comes means find frequent element from tree using counter
        """

        self.lst = []
        def inorder(root):
            if root is None:
                return 
            self.lst.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)

        freq = collections.Counter(self.lst)
        maxx = max(freq.values())

        return [key for key in freq if freq[key] == maxx]
        # -----------------------------------

        # -----------------------------------
        # Approach 2
        current_node = root
        result_lst = []
        current_streak = 0
        current_num = float("inf")
        max_streak = 0

        while current_node:
            if current_node.left:
                neighbor = current_node.left
                while neighbor.right is not None:
                    neighbor = neighbor.right
                neighbor.right = current_node

                tmp = current_node.left
                current_node.left = None
                current_node = tmp

            else:
                """
                .Since we deleted the left pointer when we were done processing in the previous if-block,
                'we know that we only reach this else case
                if we've already processed this node
                therefore do the value processing here'
                and move to the right neighbor afterward
                """
                if current_node.val == current_num:
                    current_streak += 1
                else:
                    current_streak = 0
                    current_num = current_node.val
                
                if current_streak == max_streak:
                    result_lst.append(current_num)
                elif current_streak > max_streak:
                    max_streak = current_streak
                    result_lst = [current_num]
                
                current_node = current_node.right
        return result_lst
        # -----------------------------------
