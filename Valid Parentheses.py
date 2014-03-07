class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = [0]
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')'and stack.pop() != '(':
                    return False
            elif s[i] == ']'and stack.pop() != '[':
                    return False
            elif s[i] == '}'and stack.pop() != '{':
                    return False
        return len(stack) == 1
