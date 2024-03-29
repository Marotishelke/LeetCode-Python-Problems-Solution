class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the maximum the element
        max_val = max(nums)

        # Initialize variables
        ans = 0
        left = 0
        count = 0

        # Iterate through array
        for num in nums:
            if num == max_val:
                count += 1
            while count >= k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            ans += left
        return ans
