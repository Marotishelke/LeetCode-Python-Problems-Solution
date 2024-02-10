class Solution:
    def countSubstrings(self, s: str) -> int:

        # ------------------------------------------------
        # Approach 1
        count_palindrome = 0
        length = len(s)
        for i in range(length):
            count_palindrome += 1
            for j in range(i+1, length):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    count_palindrome += 1
        return count_palindrome
        # ------------------------------------------------
