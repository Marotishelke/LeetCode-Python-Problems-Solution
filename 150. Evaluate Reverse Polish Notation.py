class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for token in tokens:
            if token in '+-/*':
                num1 = self.stack.pop()
                num2 = self.stack.pop()

                if token == '+':
                    num = num2 + num1
                elif token == '-':
                    num = num2 - num1
                elif token == '/':
                    num = int(num2 / num1)
                elif token == '*':
                    num = num2 * num1
                self.stack.append(num)
            else:
                self.stack.append(int(token))

        return self.stack[-1]
