class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        q = {}
        res = 0
        for i in range(len(s)):
            q[s[i]] = 1+ q.get(s[i], 0)
            while (i-l +1) - max(q.values())> k:
                q[s[l]] -=1
                l +=1
            res = max((i - l +1), res) 
        return res           
