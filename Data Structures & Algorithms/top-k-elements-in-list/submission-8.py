class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n ={}
        p = []
        for i in nums:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        for w,e in n.items():
                p.append([e,w])
        p.sort()
        r = []
        while len(r) < k:
            r.append(p.pop()[1])
        return r
