class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        # ----------------------------------
        # Approach 1
        res = float('-inf')
        n = len(nums)
        for i in range(k+1):
            for j in range(k, n):
                if i <= k and k <= j:
                   subarray = min(nums[i:j+1]) * (j - i + 1) 
                   if res < subarray:
                       res = subarray
        return res
        # ----------------------------------

        # ----------------------------------
        # Approach 2
        left, right = k, k
        min_val = nums[k]
        max_score = min_val
        
        while left > 0 or right < len(nums) - 1:
            if left == 0 or (right < len(nums) - 1 and nums[right + 1] > nums[left - 1]):
                right += 1
            else:
                left -= 1
            min_val = min(min_val, nums[left], nums[right])
            max_score = max(max_score, min_val * (right - left + 1))
        
        return max_score
        # ----------------------------------
