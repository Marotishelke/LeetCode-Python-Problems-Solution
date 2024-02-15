class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        total_perimeter = -1

        for num in nums:
            if num < summ:
                total_perimeter = num + summ
            summ += num
        
        return total_perimeter
