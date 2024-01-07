from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
            Case 1:- If len(nums) >= 3 and diff betw two consecutive elements is same
        """
        n = len(nums)
        number_arithmetic_slices = 0

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    number_arithmetic_slices += dp[j][diff]
        
        return number_arithmetic_slices
