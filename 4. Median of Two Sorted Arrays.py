"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        nums = []

        ind1 =0   
        ind2 = 0

        # Merge nums1 and nums2 into nums in sorted order
        while(ind1 < n1 and ind2 < n2):
            if nums1[ind1] < nums2[ind2]:
                nums.append(nums1[ind1])
                ind1 += 1
            else:
                nums.append(nums2[ind2])
                ind2 += 1
        
        # If there are remaining elements in nums1, append them to nums
        while(ind1 < n1):
            nums.append(nums1[ind1])
            ind1 += 1 

        # If there are remaining elements in nums2, append them to nums
        while(ind2 < n2):
            nums.append(nums2[ind2])
            ind2 += 1    

        # Calculate the median
        if n % 2 == 0:
            print(f'{(nums[n//2] + nums[(n-1)//2] )/2:.4f}')
            return (nums[n//2] + nums[(n-1)//2] ) / 2
        return nums[n//2]
