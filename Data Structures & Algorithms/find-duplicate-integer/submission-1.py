class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        for num in nums:
            if d[num] !=1:
                return num


        