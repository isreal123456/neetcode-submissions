class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            n = (l + r) // 2
            re = 0

            for i in piles:
                re += (i + n - 1) // n

            if re > h:
                l = n + 1
            else:
                r = n

        return l