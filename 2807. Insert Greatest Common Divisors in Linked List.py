# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # ----------------------------Function To Find Greatest Common Divisor-----------------------------------
    def greatest_common_divisior(self, num1, num2):
        if num2 == 0:
            return num1
        return self.greatest_common_divisior(num2, num1 % num2)
        
    # ------------------------------------------------------------------------------------------------------

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while(temp.next):
            num = self.greatest_common_divisior(temp.val, temp.next.val)
            temp_node = ListNode(num)
            temp_node.next = temp.next
            temp.next = temp_node
            temp = temp_node.next
        return head
