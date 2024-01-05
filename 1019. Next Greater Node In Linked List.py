# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """ Step 1: Convert Linked List to list
        Step 2: Create stack and add index into that
        """
        
        ll = []
        curr = head
        # Step 1: Convert Linked list to List
        while(curr):
            ll.append(curr.val)
            curr = curr.next
        
        n = len(ll)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and ll[i] > ll[stack[-1]]:
                j = stack.pop()
                answer[j] = ll[i]
            stack.append(i)
        return answer
