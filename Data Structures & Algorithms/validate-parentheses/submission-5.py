class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = { ')':'(', '}':'{', ']':'['}
        stack = []
        for b in s:
            if b in dict1 :
                if stack and stack[-1] == dict1[b]:
                    
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(b)
                    
                
                 

            

        if len(stack) == 0:
            return True
        else:
            return False 
        


        