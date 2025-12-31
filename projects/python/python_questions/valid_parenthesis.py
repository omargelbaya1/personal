# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(","]":"[","}":"{"}

        for c in s:
            print(stack)
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 
        return True if not stack else False

# Example usage:
solution = Solution()
print(solution.isValid("()"))          # True
print(solution.isValid("()[]{}"))      # True
print(solution.isValid("(]"))          # False
print(solution.isValid("([)]"))        # False


#Another solution:
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''