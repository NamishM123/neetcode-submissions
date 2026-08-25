class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for char in s:
            if char.isalnum():
                word+=char
        txt = word.lower()
        if txt == txt[::-1]:
            return True
        return False
        