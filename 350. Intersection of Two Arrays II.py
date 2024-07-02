""" 350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # --------------------------------------------------------------------------------------------
        # Approach 3
        # Hash Map to store numbers and their counts
        hash_map = collections.Counter(nums1)
        intersection_lst = []

        # Checking which numbers from nums2 are in Hash map those are storing in intersection list
        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                intersection_lst.append(num)
                hash_map[num] -= 1
        return intersection_lst
        # --------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------
        # Approach 2
        nums = []

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                nums.append(nums1[i])
                i += 1
                j += 1
            
            elif nums1[i] < nums2[j]:
                i += 1
            
            else:
                j += 1
        return nums
        # --------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------

        # Approach 1
        lst = []
        for i in nums1:
            if i in nums2:
                lst.append(i)
                nums2.remove(i)
        return lst
        # --------------------------------------------------------------------------------------------
