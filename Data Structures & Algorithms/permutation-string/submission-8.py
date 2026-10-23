class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        l = 0
        r = len(s1)
        while r <= len(s2):
            o = s2[l:r]
            if "".join(sorted(s2[l:r])) == s1:
                return True
            l +=1
            r +=1 
        return False
