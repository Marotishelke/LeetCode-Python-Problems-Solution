class Solution:
    def countHomogenous(self, s: str) -> int:
        # -------------------------------------
        # Approach 1
        left = 0
        res = 0

        for right in range(len(s)):
            if s[left] == s[right]:
                res += right - left + 1
            else:
                res += 1
                left = right
        return res % (10 ** 9 + 7)
        # -------------------------------------
        
        # -------------------------------------
        # Approach 2
        res = 0
        for _, stri in groupby(s):
            n = len(list(stri))
            res += n * (n + 1) // 2
        return res % (pow(10, 9) + 7)
        # -------------------------------------
