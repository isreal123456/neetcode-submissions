class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        j = Counter()
        for u in words:
            for b in u:
                j[b] += 1
        p = 1       
        for n in j.values():
            if n % len(words) != 0:
                return False
        return True