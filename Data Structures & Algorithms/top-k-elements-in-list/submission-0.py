class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        group = {}

        for w in range(len(nums)):
            key = nums[w]
            group[key] = nums.count(key)

        sgroup = dict(sorted(group.items(), key=lambda item: item[1], reverse=True))

        return list(sgroup.keys())[:k]
        