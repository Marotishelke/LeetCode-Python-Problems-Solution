class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # -----------------------------------------------
        # Approach 2
        start = 0
        prefix_zeros = 0
        current_sum = 0
        total_count = 0

        # Loop through the array using end pointer
        for end, num in enumerate(nums):
            # Add current element to the sum
            current_sum += num

            # Slide the window while condition is met
            while start < end and (nums[start] == 0 or current_sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                
                current_sum -= nums[start]
                start += 1
            
            # Count subarrays when window sum matches the goal
            if current_sum == goal:
                total_count += 1 + prefix_zeros
            
        return total_count
        # -----------------------------------------------

        # -----------------------------------------------
        # Approach 2
        num_subarrays = 0
        curr_sum = 0

        # To store the frequency of prefix sum
        freq = {}

        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                num_subarrays += 1
            
            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if curr_sum - goal in freq:
                num_subarrays += freq[curr_sum - goal]
            
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        return num_subarrays
        # -----------------------------------------------

        # -----------------------------------------------
        # Approach 1  (Time Limit Exceeded)
        """num_subarrays = 0
        size = len(nums)

        for i in range(size):
            if nums[i] == goal:
                num_subarrays += 1
            
            summ = nums[i]
            for j in range(i+1, size):
                summ += nums[j]
                if summ == goal:
                    num_subarrays += 1
                

        return num_subarrays"""
        # -----------------------------------------------
