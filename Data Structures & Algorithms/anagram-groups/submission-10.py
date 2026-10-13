class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for i in strs:
            n = ''.join(sorted(i))
            if n in g.keys():
                g[n].append(i)
            else:
                g[n] = [i]
        return list(g.values())