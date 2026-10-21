class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        o = 0
        for i in range(len(prices)):
            r=i +1
            while r < len(prices):
                u = prices[r] - prices[i] 
                o = max(u, o)
                r +=1
        return o
