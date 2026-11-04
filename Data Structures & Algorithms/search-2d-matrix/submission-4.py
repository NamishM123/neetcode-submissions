class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maybe iterate thru each row 
        # if taret in row return True else False?
        for num in matrix:
            if target in num:
                return True 


        return False
        
                    



        