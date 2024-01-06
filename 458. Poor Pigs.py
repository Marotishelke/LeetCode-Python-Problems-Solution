class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # -----------------------------------------
        # APPROACH 1
        return ceil(log2(buckets) / log2(minutesToTest//minutesToDie + 1))
        # -----------------------------------------

        # -----------------------------------------
        # APPROACH 2
        t = minutesToTest // minutesToDie
        x = 0
        while (t + 1) ** x < buckets:
            x += 1
        return x
        # -----------------------------------------
