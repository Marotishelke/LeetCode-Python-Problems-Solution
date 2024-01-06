class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # -----------------------------------
        # Approach 1
        start, end = -1, -1

        # Check forward direction
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        if start == -1:
            return [-1, -1]
        
        # Check Backward direction 
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                end = i
                break
        
        return [start, end]
        # -----------------------------------

        # -----------------------------------
        # Approach 2
        def binary_search(nums, target, left):
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index

        left_index = binary_search(nums, target, left=True)
        right_index = binary_search(nums, target, left=False)

        return [left_index, right_index]
        # -----------------------------------
