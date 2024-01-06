class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # --------------------------------------------
        # Approach 1
        cnt_good_pairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt_good_pairs += 1
        return cnt_good_pairs
        # --------------------------------------------


        # --------------------------------------------
        # Approach 2
        return sum([(value * (value-1))//2 for value in collections.Counter(nums).values()])
        # --------------------------------------------
