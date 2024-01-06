class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        visited, count, multiplier = None, 0, -1

        for i in nums:
            if i!=visited:
                multiplier += 1
                visited = i
                
            count+= multiplier

        return count
