class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "{":"}", "[":"]"}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(pairs[i])
            elif i in pairs.values():
                if len(stack) == 0:
                    return False
                elif i == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

            