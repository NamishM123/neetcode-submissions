from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0

        while right <= len(s2) - len(s1):
            j = 0
            dict1 = Counter(s1)

            while (
                j < len(s1)
                and dict1[s2[right + j]] > 0
            ):
                dict1[s2[right + j]] -= 1
                j += 1

            if j == len(s1):
                return True

            right += 1

        return False