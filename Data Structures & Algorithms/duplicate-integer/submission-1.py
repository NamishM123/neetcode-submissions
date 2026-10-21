class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        new_list = []
        for i in range (x):
            
            if nums[i] in new_list:
            
                return True
            new_list.append(nums[i])
        
        return False

            