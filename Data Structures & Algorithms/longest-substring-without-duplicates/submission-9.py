class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = set()
        l =0
        r = 0
        for i in range(len(s)):
            while s[i] in n:
                n.remove(s[l])
                l+=1
            k = i - l +1 
            r = max(k,r)
            n.add(s[i])
        return r