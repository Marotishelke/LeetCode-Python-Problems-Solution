import numpy
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        # ---------------------------------------------
        # Approach 1 -- Time Limit Excceded Error 
        """result = []
        for i in range(len(nums)):
            sum_ = 0
            for j in range(len(nums)):
                sum_ = sum_ + abs(nums[i] - nums[j])
            result.append(sum_)
        return result"""
        # ---------------------------------------------

        # ---------------------------------------------
        # Approach 2
        result = []
        arr = numpy.array(nums)
        for i in nums:
            result.append(sum(abs(arr - i)))

        return result
        # ---------------------------------------------

        # ---------------------------------------------
        # Approach 3
        sm = 0
        n = len(nums)
        result = []
        total = sum(nums)

        for i in range(n):
            sm += nums[i]
            x = ((i + 1)*nums[i]-sm) + (total - sm - (n - i - 1) * nums[i])
            result.append(x)
            
        return result
        # ---------------------------------------------
        
