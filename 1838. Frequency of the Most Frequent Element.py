class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        max_frequency = 0
        current_sum = 0

        # Step  2: Use two pointers
        left = 0
        for right in range(len(nums)):
            # Include the current element in the subarray sum
            current_sum += nums[right]

            # Step 3: CHeck if the current subarray vilotes the conditiion (sum + k < nums[right] * length)
            while current_sum + k < nums[right] * (right - left + 1):
                # Adjust the subarray sum by removing the leftmost element
                current_sum -= nums[left]

                # Move the left pointer to the right
                left += 1
            
            # Update the maximum frequency based on the current subarray length
            max_frequency = max(max_frequency, right - left + 1)
        return max_frequency
