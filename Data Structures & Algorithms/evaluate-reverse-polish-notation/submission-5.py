class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = int(tokens[0])
        for idx, token in enumerate(tokens, 1):
            match token:
                case '+':
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                case '-':
                    right, left = stack.pop(), stack.pop()
                    result =  left - right
                    stack.append(result)
                case '*':
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                case '/':
                    right, left = stack.pop(), stack.pop()
                    result = int(left / right)
                    stack.append(result)
                case _:
                    stack.append(int(token))

        return result

