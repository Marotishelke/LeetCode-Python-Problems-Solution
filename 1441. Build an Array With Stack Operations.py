class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # -------------------------------------------------
        # Approach 1
        stack = []
        res = []
        ind = 0
        for i in range(1, n+1):
            res.append('Push')
            stack.append(i)
            
            if ind < len(target) and stack[-1] == target[ind]:
                ind += 1
            elif ind < len(target) and stack[-1] < target[ind]:
                stack.pop()
                res.append('Pop')
            
            if stack == target:
                return res
        # -------------------------------------------------

        # -------------------------------------------------
        # Approach 2
        operation_stack = []
        current_num = 1
        ind = 0

        while(ind < len(target) and current_num <= n):
            if current_num == target[ind]:
                operation_stack.append('Push')
                ind += 1
            else:
                operation_stack.extend(['Push', 'Pop'])
            current_num += 1
        return operation_stack
        # -------------------------------------------------
