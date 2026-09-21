class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            # if closing bracket
            if char in mapping:
                top = stack.pop() if stack else '#'

                if mapping[char] != top:
                    return False

            # if opening bracket
            else:
                stack.append(char)

        return not stack        