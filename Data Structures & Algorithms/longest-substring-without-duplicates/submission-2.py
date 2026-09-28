class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ''
        result = 0
        for i in range(len(s)):
            if s[i] in current:
                index = current.find(s[i])
                current = current[index + 1:] + s[i]
            else:
                current += s[i]
            result = max(len(current), result)
        return result