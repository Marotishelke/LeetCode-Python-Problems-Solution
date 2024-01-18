class Solution:
    def climbStairs(self, n: int) -> int:
        # --------------------------------------
        # Step 1 : If n <= 2 return n
        if n <= 2:
            return n
        # ---------------------------------------

        # Step 2 : If n > 2 Then simply use fibonacii series to find distinct ways to climb to the top
        a = 1
        b = 1
        x = 0
        for i in range(2, n + 1):
            x = a + b
            a = b
            b = x
        return x
        

