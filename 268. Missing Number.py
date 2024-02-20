class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # -----------------------------
        # Approach 1  O(nlgon)
        """ n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        """
        # -----------------------------

        # -----------------------------
        # Approach 2  O(nlgon)
        """nums.sort()
        i = 0
        while (i < len(nums)):
            if i != nums[i]:
                return i
            i += 1
        return i
        """
        # -----------------------------

        # -----------------------------
        # Approach 3 O(n)
        n = len(nums)
        return abs(sum(nums) - (n * (n + 1)) // 2)
        # -----------------------------
