class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        unorder_map = {}
        left = 0
        n = len(nums)

        for right in range(n):
            unorder_map[nums[right]] = unorder_map.get(nums[right], 0) + 1
            if unorder_map[nums[right]] > k:
                while nums[left] != nums[right]:
                    unorder_map[nums[left]] -= 1
                    left += 1
                unorder_map[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
