import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # ----------------------------------------------------------
        # Approach 1: Sort the array and find max and second max
        # ----------------------------------------------------------
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
    

        # -----------------------------------------------------------
        # Approach 2: Use heapq and find largest & 2nd largest 
        # -----------------------------------------------------------
        
        largest_elements = heapq.nlargest(2, nums)
        return (largest_elements[0] - 1) * (largest_elements[1] - 1)

        # ---------------------------------Approach 3 ----------------
        """ Step1: Find Max And 2nd Max from Array 
            Step2: Multiply Max & 2nd_Max
        """
        # ------------------------------------------------------------
        maxx = 0
        maxx2 = 0
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxx2 = maxx
                maxx = nums[i]
            else:
                maxx2 = max(maxx2, nums[i])
        return (maxx - 1) * (maxx2 - 1)


        
