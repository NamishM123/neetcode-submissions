from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = []

        if not nums:
            return False

        for i in range(len(nums)):
            if nums[i] in list1:
                return True

            list1.append(nums[i])

        return False