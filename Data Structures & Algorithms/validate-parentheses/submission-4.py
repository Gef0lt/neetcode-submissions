class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack:
                return False
            else:
                if stack[-1] == '{' and char != '}' or stack[-1] == '(' and char != ')' or stack[-1] == '[' and char != ']':
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False