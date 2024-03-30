class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        def solve(nums: List[int], k: int) -> int:
            ans = 0
            n = len(nums)
            count = defaultdict(int)
            diff = 0

            left = 0
            for right in range(n):
                count[nums[right]] += 1
                if count[nums[right]] == 1:
                    diff += 1
                
                while diff > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        diff -= 1
                    left += 1
                
                ans += (right - left + 1)
            return ans

        return solve(nums, k) - solve(nums, k - 1)
