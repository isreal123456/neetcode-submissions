class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {}

        for i in nums:
            t[i] = t.get(i, 0) + 1

        s = sorted(t.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in s[:k]] 
