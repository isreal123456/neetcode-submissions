class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in g:
                g[s] = []
            g[s].append(i)
        return(list(g.values()))