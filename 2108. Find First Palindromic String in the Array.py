class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # -------------------------------
        # Approach 1
        length = len(words)
        for i in range(length):
            if words[i] == words[i][::-1]:
                return words[i]
        return ''
        # -------------------------------
