"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.score = 0
        def funct_to_delete_substr(strr: str, substr: str, points: int):
            stack_remaining_str = []
            for char in strr:
                if char == substr[-1] and stack_remaining_str and stack_remaining_str[-1] == substr[0]:
                    self.score += points
                    stack_remaining_str.pop()
                else:
                    stack_remaining_str.append(char)
            return ''.join(stack_remaining_str)

        
        if x > y:
            strr = funct_to_delete_substr(s, 'ab', x)
            strr = funct_to_delete_substr(strr, 'ba', y)
        else:
            strr = funct_to_delete_substr(s, 'ba', y)
            strr = funct_to_delete_substr(strr, 'ab', x)
        
        return self.score
