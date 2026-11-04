class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maybe iterate thru each row 
        # if taret in row return True else False?
        length = len(matrix) * len(matrix[0])
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right  = length-1
        while left<=right:
            middle = (left+right)//2
            r = middle // cols 
            c = middle % cols 
            val = matrix[r][c]
            if target == val:
                return True 

            elif val > target:
                right = middle -1
            else:
                left = middle +1

        return False
        
        
                    



        