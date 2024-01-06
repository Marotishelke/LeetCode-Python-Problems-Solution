class Solution:
    def longestPalindrome(self, s: str) -> str:
        # -------------------------------
        # Approach 1
        if len(s) <= 1:
            return s
        
        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    max_str = s[i:j+1]
        return max_str
        # -------------------------------

        # -------------------------------
        # Approach 2
        def is_palindrome(s):
            return s == s[::-1]
        
        palindromic_substring = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_string = s[i:j+1]
                if is_palindrome(sub_string):
                    if len(palindromic_substring) > len(sub_string):
                        continue
                    else:
                        palindromic_substring = sub_string
        return palindromic_substring
        # -------------------------------
