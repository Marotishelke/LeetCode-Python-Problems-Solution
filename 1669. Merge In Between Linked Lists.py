# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Approach 1
        prev = None
        forward = None
        temp = list1
        length = 1

        while(temp):
            if length == a:
                prev = temp
                break
            length += 1
            temp = temp.next
        
        length -= 1

        while(temp):
            if length == b:
                forward = temp
                break
            length += 1
            temp = temp.next
        
        temp2 = list2
        while(temp2.next):
            temp2 = temp2.next
        
        temp2.next = temp.next
        prev.next = list2
        return list1
