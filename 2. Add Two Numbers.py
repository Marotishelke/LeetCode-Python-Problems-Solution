"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a new ListNode to store the result
        head = ListNode()
        # Initialize a pointer 'current' to the head of the result list
        current = head
        # Initialize carry to store any overflow from addition
        carry = 0

        # Traverse both input lists until both are exhausted
        while l1 is not None or l2 is not None:
            # Initialize summ to store the sum of current digits and carry
            summ = 0
            # Add l1 value to summ if l1 is not None, then move l1 to the next node
            if l1 is not None:
                summ += l1.val
                l1 = l1.next
            # Add l2 value to summ if l2 is not None, then move l2 to the next node
            if l2 is not None:
                summ += l2.val
                l2 = l2.next
            # Add carry from the previous step to summ
            summ += carry
            # Update carry for the next digit sum
            carry = summ // 10
            # Append a new node with the last digit of summ to the result list
            current.next = ListNode(summ % 10)
            # Move the 'current' pointer to the newly added node
            current = current.next

        # After loop, if there's any remaining carry, add it as a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the head of the result list (skip the dummy node)
        return head.next
