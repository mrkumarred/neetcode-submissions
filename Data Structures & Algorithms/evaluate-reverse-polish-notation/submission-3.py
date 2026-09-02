class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                right = stack.pop()   # later operand (right side)
                left = stack.pop()    # earlier operand (left side)

                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:  # '/'
                    # // floors toward -inf; RPN needs truncation toward zero.
                    # When remainder != 0 AND signs differ, the floor is one low → add 1.
                    q = left // right
                    if left % right != 0 and (left < 0) != (right < 0):
                        q += 1
                    result = q

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]