"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Intialize left ptr and max length and hash map
        left = 0
        max_len = 0
        hash_map = {}

        # Iterate loop to visit characters of s
        for right in range(len(s)):

            # Check the char is present in hash map and left ptr should less than last seen index of char
            if s[right] in hash_map and left <= hash_map[s[right]]:
                left = hash_map[s[right]] + 1
            
            # Add char in hash map with index
            hash_map[s[right]] = right

            # find maximum length of substring
            max_len = max(max_len, right - left + 1)
        
        return max_len
