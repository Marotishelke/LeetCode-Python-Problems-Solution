class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # -----------------------------------------
        # Approach 1
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            # nums2[j] < nums1[i]
            else:                    
                j += 1
        return -1 
        # -----------------------------------------

        # -----------------------------------------
        # Approach 2
        """hash_map = collections.defaultdict(int)

        for num in nums1:
            hash_map[num] += 1
        
        for num in nums2:
            if hash_map[num] > 0:
                return num
        return -1"""
        # -----------------------------------------

        # -----------------------------------------
        # Approach 3
        """hash_set = set(nums1)

        for num in nums2:
            if num in nums1:
                return num
        return -1"""
        # -----------------------------------------
