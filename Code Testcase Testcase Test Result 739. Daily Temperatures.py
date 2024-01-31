class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # -----------------------------------------------------------
        # Approach 1
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for ind, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp:
                index = stack.pop()
                answer[index] = ind - index    
            stack.append(ind)

        return answer
        # -----------------------------------------------------------
