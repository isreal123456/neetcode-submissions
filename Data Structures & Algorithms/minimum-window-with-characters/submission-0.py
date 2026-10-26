from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        countT = Counter(t)

        res, resLen = [-1, -1], float("infinity")
        l = 0
        h = 0
        n = len(countT)

        for r in range(len(s)):
            w = s[r]
            window[w] = 1 + window.get(w, 0)

            if w in countT and window[w] == countT[w]:
                h += 1

            while h == n:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    h -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""