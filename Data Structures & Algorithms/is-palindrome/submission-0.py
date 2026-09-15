class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right :
            # 1. Skip non-alphanumeric from the left
            while left < right and not s[left].isalnum():
                left += 1

            # 2. Skip non-alphanumeric from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # 3. Compare the valid characters in lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
            