class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # ------------------------------------------
        # Approach 1
        stack = [num for num in range(1, k+1)]
        operation_cnt = 0
        for i in range(len(nums)-1, -1, -1):
            operation_cnt += 1
            if nums[i] in stack:
                stack.remove(nums[i])
            if len(stack) == 0:
                break
            
        return operation_cnt
        # ------------------------------------------

        # ------------------------------------------
        # Approach 2
        """
        We are storing only good (numbers which will be in sequence 1...k) numbers in set.
        """
        s = set()
        ind = 0
        while(len(s) < k):
            ind += 1
            if nums[-ind] <= k:
                s.add(nums[-ind])
        return ind
        # ------------------------------------------
