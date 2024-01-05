class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # -----------------------------------------------
        # Hash map 
        nums_dict = collections.Counter(nums)
        operation_cnt = 0
        for val in nums_dict.values():
            # If there is unique value present then return -1
            if val == 1:
                return -1
            
            # If there are duplicates are there 
            operation_cnt += (val + 2) // 3
            
        return operation_cnt 
        # -----------------------------------------------     
