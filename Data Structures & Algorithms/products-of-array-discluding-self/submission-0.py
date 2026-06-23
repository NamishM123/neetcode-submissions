class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1=[]
        
        for i in range (len(nums)):
            na=1
            for j in range(len(nums)):
                if i != j:
                    na = na*nums[j]
            list1.append(na)
        
        return list1


        