class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # Approach 1
        n = len(cost)

        @cache
        def dfs(i, t):
            if t <= 0:
                return 0
            if i == n:
                return float('inf')
            return min(dfs(i+1, t), dfs(i+1, t-time[i]-1) + cost[i])

        res = dfs(0, n)
        return res

        # Approach 2
        n = len(cost)
        dp = [float('inf')] * (n + 1) # Create a dynamic programming array to store minimum cost
        dp[0] = 0

        # Loop for each  wall
        for i in range(n):
            # Loop through the dynamaic programming array in reverse order
            for j in range(n, 0, -1):
                """
                    Calculate the minimum coast to paint 'j' walls using current wall 'i'
                    The minimum cost at 'j' is the minimum of:
                    - The cost of painting the current wall 'i' + the cost of painting the previous walls (dp[j - time[i] - 1])
                    - The cost of painting the previous walls without using the current wall 'i' (dp[j])      
               """
                dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])

        return dp[n]  # The minimum cost to paint all 'n' walls is stored in dp[n]
