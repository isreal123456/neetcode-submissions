class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t)> len(s):
            return ""

        window = {}
        countT = Counter(t)

        res, resLen = [0, 0], float("infinity") 
        l = 0
        h = 0
        n = len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                h += 1
            while h == n:
                if  (r-l +1) < resLen:
                    resLen = (r-l +1)
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    h -= 1
                l += 1
        l,r = res
        return s[l : r + 1] if resLen != float("infinity") else ""