class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        def is_start(n):
            return n - 1 not in nums

        def count_length(n):
            length = 1
            while n + 1 in nums:
                n += 1
                length += 1
            return length

        for n in nums:
            if is_start(n):
                longest = max(longest, count_length(n))

        return longest
                
        

            

        
        