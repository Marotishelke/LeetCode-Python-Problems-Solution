class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # ---------------------------------------------------------------
        # Sort both the list
        g.sort()
        s.sort()
        # ---------------------------------------------------------------

        cookies_cnt = 0
        i, j = 0, 0
        while(i < len(g) and j < len(s)):
            if s[j] >= g[i]:
                cookies_cnt += 1
                i += 1
            j += 1
        return cookies_cnt
