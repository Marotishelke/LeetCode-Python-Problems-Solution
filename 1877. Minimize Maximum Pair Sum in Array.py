class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array in ascending order
        nums.sort()

        # Initialize pointers at the start end of the sorted array
        left, right = 0, len(nums) - 1

        # Initialize a variable to store the minimum of the maximum pair sum
        min_max_pair_sum = float('-inf')

        # Step 2: Iterate untill the 
        while left < right:
            # Calculate the current pair sum
            current_pair_sum = nums[left] + nums[right]

            # Update the minimum of the maximum pair sum
            min_max_pair_sum = max(min_max_pair_sum, current_pair_sum)

            #Move the pointers towrads the middle
            left += 1
            right -= 1
        return min_max_pair_sum
