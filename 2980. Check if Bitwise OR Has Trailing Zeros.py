class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # Length of array
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                bitwise_or = nums[i] | nums[j]
                
                # Check if the bitwise_or has at least one trailing zero
                # print(str(bitwise_or)[-1])
                if bin(bitwise_or)[-1] == '0':
                    return True
        return False
