class Solution:
    def closing(self, char: str):
        if char == "]":
            return "["
        if char == ")":
            return "("
        if char == "}":
            return "{"
    def isValid(self, s: str) -> bool:
        stack = list()
        for x in s:
            if len(stack) > 0 and self.closing(x) == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        if len(stack) == 0:
            return True
        else:
            return False