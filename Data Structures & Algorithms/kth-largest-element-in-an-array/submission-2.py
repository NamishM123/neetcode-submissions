class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = sorted(nums)
        n= l[-k]
        return n


        