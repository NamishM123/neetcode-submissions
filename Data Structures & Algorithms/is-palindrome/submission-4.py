class Solution:
    def isPalindrome(self, s: str) -> bool:
        word =""
        for char in s:
            if char.isalnum():
                char = char.lower()
                word+=char
        list1 = list(word)
        list2 = list1[::-1]
        print(list1)
        print(list2)
        return (list1 == list2)