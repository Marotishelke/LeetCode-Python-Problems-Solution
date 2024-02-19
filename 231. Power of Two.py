        # ------------------------------
        # Approach 1
        power = 0
        while(2**power <= n):
            if 2**power == n:
                return True
            power += 1
        return False
        # ------------------------------

        # ------------------------------
        # Approach 2
        if n <= 0:
            return False
        return ((n & (n - 1)) == 0);
        # ------------------------------
