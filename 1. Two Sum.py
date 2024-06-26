"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}

    # Iterate the loop to find indexs to get sum equal to target
    for i in range(len(nums)):

        # subtract the current value from target
        complement = target - nums[i]

        # Searching in hash map
        if complement in hash_map:
            return i, hash_map[complement]
        hash_map[nums[i]] = i
