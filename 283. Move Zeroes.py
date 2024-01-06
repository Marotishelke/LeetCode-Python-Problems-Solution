class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        length = len(nums)
        while(i < length and j < length):
            if nums[i] != 0 and nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]  # Swapping the numbers
                j += 1
            if nums[j] != 0:
                j += 1
            i += 1
