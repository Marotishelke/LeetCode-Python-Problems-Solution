class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # ----------------------
        # Approach 1
        i = 0
        while True:
            fourth_root = 4 ** i
            if fourth_root == n:
                return True
            elif fourth_root > n:
                return False
            i += 1
        # ----------------------

        # ----------------------
        # Approach 2
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
        # ----------------------
