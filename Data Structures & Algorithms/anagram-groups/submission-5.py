class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            k = "".join(sorted(word))

            if k not in groups:
                groups[k] = []

            groups[k].append(word)
        # print(groups)
        return list(groups.values())