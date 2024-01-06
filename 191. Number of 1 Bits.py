class Solution:
    def hammingWeight(self, n: int) -> int:
        # ----------------Approach 1----------------
        count = 0
        while n:
            count += n % 2
            n //= 2
        return count
        # ------------------------------------------

        # ----------------Approach 1----------------
        return bin(n).count('1')
        # ------------------------------------------
