class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        r , q = {}, {}
        for i in range(len(s)):
            r[s[i]] = 1+ r.get(s[i], 0)
            q[t[i]] = 1+ q.get(t[i], 0)
        print(r,q)
        return r == q