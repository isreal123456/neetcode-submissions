class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        o = 0 
        p = 1
        i = 0
        while p < len(prices):
            if prices[o] < prices[p]:
                e = prices[p] - prices[o]
                i= max(e, i)
            else:
                o = p
            p += 1
        return i