class Solution:
    def integerBreak(self, n: int) -> int:

        # -------------------------------------
        # Approach 1
        if n <= 3:
            return n-1
        quotient = n//3
        remainder = n % 3
        if remainder == 0:
            return 3 ** quotient
        if remainder == 1:
            return (3 ** (quotient-1)) * 4
        else:
            return (3 ** quotient) * 2
        # -------------------------------------

        # -------------------------------------
        # Approach 2
        if n <= 3:
            return n-1
        mul = 1
        while(n > 4):
            mul *= 3
            n -= 3
        return mul * n
        # -------------------------------------
