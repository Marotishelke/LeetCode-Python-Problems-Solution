class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # --------------------------------------------------------------------
        # Approach 2
        n = len(nums)
        duplicate = 0
        missing = 0

        map_counter = {i : 1 for i in range(1, n + 1)}
        for num in nums:
            map_counter[num] -= 1
        
        
        for key in map_counter:
            if map_counter[key] == -1:
                duplicate = key
            elif map_counter[key] == 1:
                missing = key
        return [duplicate, missing]
        # --------------------------------------------------------------------


        # --------------------------------------------------------------------
        """
        # Approach 1
        Step1 : Travel one loop and check current number Count is 2 or 0
        Step2 : If count is 2 then it is duplicate
        Step3 : if the count is 0 the it is missing
        """
        # --------------------------------------------------------------------
        duplicate = -1
        missing = -1
        n = len(nums)

        for i in range(1, n + 1):
            count = nums.count(i)
            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i
        return [duplicate, missing]
