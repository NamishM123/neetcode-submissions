class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = float('inf')
        result = float('-inf')
        for price in prices:
            result  = max(result, price - mins)
            

            mins = min(price, mins)

        if result<0:
            return 0
        else:
            return result

        



        