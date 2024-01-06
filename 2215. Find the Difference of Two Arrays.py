class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        res = [[], []]

        for i in nums1:
            if i not in nums2:
                res[0].append(i)
        
        for i in nums2:
            if i not in nums1:
                res[1].append(i)
        return res
