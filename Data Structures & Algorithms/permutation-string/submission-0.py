class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        b = ""
        l = 0
        r = len(s1)
        p = 0
        while r <= len(s2):
            o = s2[l:r]
            if "".join(sorted(o)) == s1:
                p += 1
            elif "".join(sorted(o)) != s1:
                p -= 0
            l +=1
            r +=1 
        return (p >= 1)
