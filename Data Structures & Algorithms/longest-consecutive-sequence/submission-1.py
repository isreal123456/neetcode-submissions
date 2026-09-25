class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        l = 0
        for i in n:
            if i - 1 not in n:
                m = 0 
                while m + i in n:
                    m += 1
                l = max(l, m)
        return l 

