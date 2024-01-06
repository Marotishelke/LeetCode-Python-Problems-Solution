class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Approach 1
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n -1
        return abs(res)
        
