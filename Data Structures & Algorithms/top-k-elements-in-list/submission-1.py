class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}

        for num in nums:
            group[num] = group.get(num, 0) + 1

        sgroup = dict(sorted(group.items(), key=lambda item: item[1], reverse=True))

        return list(sgroup.keys())[:k]