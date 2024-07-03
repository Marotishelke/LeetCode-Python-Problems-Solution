You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 
"""
Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Approach 2
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
    
        nums.sort()
        n = len(nums)
        
        # Possible scenarios of adjusting elements
        # We consider adjusting:
        # 1. The first 3 elements to the smallest element
        # 2. The last 3 elements to the largest element
        # 3. A combination of first and last elements
        
        # Scenario 1: Adjust the first 3 elements to the smallest element in nums
        scenario1 = nums[n-4] - nums[0]
        
        # Scenario 2: Adjust the last 3 elements to the largest element in nums
        scenario2 = nums[n-1] - nums[3]
        
        # Scenario 3: Adjust the first 2 elements and the last element
        scenario3 = nums[n-3] - nums[1]
        
        # Scenario 4: Adjust the first element and the last 2 elements
        scenario4 = nums[n-2] - nums[2]
        
        # Find the minimum difference from all scenarios
        return min(scenario1, scenario2, scenario3, scenario4)

        # Approach 1
        print(len(nums))
        if len(nums) <= 4:
            return 0
        nums.sort()
        n = len(nums)
        # case 1:
        min1 = nums[3:][-1] - nums[3:][0]

        # case 2:
        min2 = nums[:n-3][-1] - nums[:n-3][0]

        # case 3
        min3 = nums[2:n-1][-1] - nums[2:n-1][0]

        # case 4
        min4 = nums[1:n-2][-1] - nums[1:n-2][0]

        return min(min1, min2, min3, min4)
        
