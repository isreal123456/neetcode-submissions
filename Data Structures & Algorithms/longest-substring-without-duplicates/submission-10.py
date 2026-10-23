class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= set()
        l = 0
        r =0 
        for ri in range(len(s)):
            while s[ri] in n:
                n.remove(s[l])
                l += 1
            j = ri - l+1
            r =max(j, r)
            n.add(s[ri])
        return r
