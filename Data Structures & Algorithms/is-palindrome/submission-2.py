class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s)).lower()
        return clean == clean[::-1]
        
        