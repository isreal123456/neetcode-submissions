class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        i = 0
        m = defaultdict(int)

        for n in range(len(s)):
            m[s[n]] += 1

            max_freq = max(m.values())
            q = (n - l + 1) - max_freq

            if q > k:
                m[s[l]] -= 1
                l += 1

            i = max(i, n - l + 1)

        return i