class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        l = 0 
        lst = 0 
        for r in  range(len(s)):
            while s[r]  in set1:
             
                set1.remove(s[l])
                l = l+1
                
            
            set1.add(s[r])
           
            lst = max(lst,r-l+1)
            r+=1

            
        return lst

