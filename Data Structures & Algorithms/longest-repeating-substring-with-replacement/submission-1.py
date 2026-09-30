
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        o = 0
        i = o
        m = defaultdict(int)
        
        for n in range(len(s)): 
            m[s[n]] += 1
            print (max(m.values()))
            q =(n-l+1) - max(m.values())
            if q > k:
                m[s[l]] -= 1
                l += 1
            i = max(i, n - l + 1)
        return i