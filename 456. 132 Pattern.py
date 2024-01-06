class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = nums.__len__()
        # Approach 1
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
        return False

        # Approach 2
        stack = []
        third = float('-inf')

        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
