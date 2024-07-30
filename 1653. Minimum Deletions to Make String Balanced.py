""" You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # ---------------------------------------------------
        # Approach 2
        n = len(s)
        min_deletions = 0
        b_count = 0

        # min_deletions variable represents dp[i]
        for ch in s:
            if ch == "b":
                b_count += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions
        # ---------------------------------------------------

        # ---------------------------------------------------
        # Approach 1
        char_stack = []
        delete_count = 0

        # Iterate through each character in the string
        for char in s:
            # If stack is not empty, top of stack is 'b',
            # and current char is 'a'
            if char_stack and char_stack[-1] == "b" and char == "a":
                char_stack.pop()  # Remove 'b' from stack
                delete_count += 1  # Increment deletion count
            else:
                char_stack.append(char)  # Append current character to stack

        return delete_count
        # ---------------------------------------------------
