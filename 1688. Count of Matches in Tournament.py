class Solution:
    def numberOfMatches(self, n: int) -> int:
        # ----------------------------------------------Approach 1------------------
        matches_played = 0
        while(n > 1):
            if n % 2 == 0:
                matches_played += n // 2
                n //= 2
            else:
                matches_played += (n - 1) // 2
                n = ((n - 1) // 2) + 1
        return matches_played
        
        # ---------------------------------------------------------------------------

        # --------------------------Direct Approach----------------------------------
        return n-1
        #----------------------------------------------------------------
