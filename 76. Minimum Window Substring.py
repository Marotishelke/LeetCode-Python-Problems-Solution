class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If S or T is empty
        if not s or not t:
            return ""

        dict_ = collections.defaultdict(int)
        for c in t:
            dict_[c] += 1
        
        required = len(dict_)
        l, r = 0, 0
        formed = 0

        window_counts = collections.defaultdict(int)
        ans = [-1, 0, 0]

        while(r < len(s)):
            c = s[r]
            window_counts[c] += 1

            if c in dict_ and window_counts[c] == dict_[c]:
                formed += 1
            
            while l <= r and formed == required:
                c = s[l]

                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                window_counts[c] -= 1
                if c in dict_ and window_counts[c] < dict_[c]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]
