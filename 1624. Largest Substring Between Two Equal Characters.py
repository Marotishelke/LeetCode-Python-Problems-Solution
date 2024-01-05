class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # --------------------------- Approach 1 ---------------------
        """ ans = -1

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)
        return ans
        """
        # --------------------------------------------------------------

        # --------------------------Approach 2--------------------------
        first_ind = {}
        ans = -1

        for i in range(len(s)):
            if s[i] in first_ind:
                ans = max(ans, i - first_ind[s[i]] - 1)
            else:
                first_ind[s[i]] = i
        return ans
        # ----------------------------------------------------------------
