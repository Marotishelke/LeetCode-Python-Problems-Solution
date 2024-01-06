class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Approach 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        return False
        
        # Approach 2
        first, second = float('inf'), float('inf')
        for third in nums:
            # Find First Smallest
            if third <= first:
                first = third
            # Find Second Smalles
            elif third <= second:
                second = third
            else:
                return True
        return False
