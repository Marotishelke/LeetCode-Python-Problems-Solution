class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        # ---------------------------------------
        # Approach 1
        arithmatic_triplets_cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff) :
                        arithmatic_triplets_cnt += 1
        return arithmatic_triplets_cnt
        # ---------------------------------------

        # ---------------------------------------
        # Approach 2
        seen = set()
        cnt = 0
        for num in nums:
            if num - diff in seen and num - diff * 2 in seen:
                cnt += 1
            seen.add(num)
        return cnt 
        # ---------------------------------------
