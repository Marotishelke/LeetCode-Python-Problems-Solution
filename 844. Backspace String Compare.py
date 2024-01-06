class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # --------------------------
        # Approach1
        stack1, stack2 = [], []
        for i in s:
            if i == '#' and stack1:
                stack1.pop()
            elif i != '#':
                stack1.append(i)

        for i in t:
            if i == '#' and stack2:
                stack2.pop()
            elif i != '#':
                stack2.append(i)
        return stack1 == stack2
        # --------------------------

        # --------------------------
        # Approach 2
        def backspace(str):
            ans = []
            for i in str:
                if i != '#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return ans
        
        return backspace(s) == backspace(t)
        # --------------------------
