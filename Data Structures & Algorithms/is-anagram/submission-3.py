class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        dict = {}
        for char in l1:
            dict[char] = dict.get(char,0)+1
        for char in l2:
            dict[char] = dict.get(char,0)-1
        
        for val in dict.values():
            if val != 0:
                return False
        return True
        


        
        