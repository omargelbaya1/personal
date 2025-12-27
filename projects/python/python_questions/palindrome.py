# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

#my solution is:


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        rev_s= s[::-1]

        print(s)
        print(rev_s)

        for i in range(len(s)):
            print(i,s[i].lower(),rev_s[i].lower())
            if s[i].lower() != rev_s[i].lower():
                return False

        return True
        
# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))                      # Output: False
print(solution.isPalindrome(" "))                               # Output: True              
#more Examples of code:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
