class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # --------------------------------------------
        # Approach 1 T.C :- O(nlogm) S.C. :- O(n)
        hash_set = set()

        for num in nums1:
            if num in nums2:
                hash_set.add(num)
        return list(hash_set)
        # --------------------------------------------

        # --------------------------------------------
        # Approach 2 T.C :- O(nlogn)   S.C :- O(n)
        """res = []

        # Sort Both The Array
        nums1.sort()
        nums2.sort()

        # Define Two pointers
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            # If number is present in both array and not in result array
            if nums1[i] == nums2[j] and nums1[i] not in res:
                res.append(nums1[i])
            
            # If element second array is greater than element in first array 
            # Increase the i to 1
            # Else Increase j to 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res"""
        # --------------------------------------------

        # --------------------------------------------
        # Approach 3     T.C :- O(n * m)
       """nums1 = set(nums1)
        nums2 = set(nums2)

        res = list(nums1 & nums2)
        return res"""
        # --------------------------------------------        
