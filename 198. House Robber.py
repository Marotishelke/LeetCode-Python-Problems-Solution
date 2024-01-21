class Solution:
    def rob(self, nums: List[int]) -> int:
        # ------------------------------------------------------------------  
        # Step1 :- Set variables prev and curr for tracking, and iterate through the nums array.
        # Step :- For each house, calculate the maximum money by choosing to rob or skip, updating prev and curr.
        #Step 3 :- After iteration, return the final result in curr, representing the maximum money robbed without robbing adjacent houses.
        # ------------------------------------------------------------------
        n = len(nums)
        
        prev = 0
        curr = 0
        for i in range(n):
            max_amount = max(prev + nums[i], curr)
            prev = curr
            curr = max_amount
        return curr
