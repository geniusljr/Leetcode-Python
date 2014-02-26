class Solution:
    def evalRPN(self, tokens):
        if (tokens == None or len(tokens) == 0):
            return None
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "*":
                    stack.append(first*second)
                elif token == "/":
                    stack.append(int(float(first)/second))
        return stack.pop()
    
                    
