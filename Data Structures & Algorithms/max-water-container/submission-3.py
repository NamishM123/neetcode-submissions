class Solution:
    def maxArea(self, heights: List[int]) -> int:
        list1=[]
        left = 0 
        right = len(heights)-1
        while right>left:
            width = right - left
            height = min(heights[left],heights[right])
            area = width*height
            list1.append(area)

            if heights[right]<heights[left]:
                right -=1
            else:
                left +=1
        return max(list1)

        
        