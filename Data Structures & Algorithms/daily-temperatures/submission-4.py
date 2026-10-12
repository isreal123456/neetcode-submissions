class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s =[]
        for i in range(len(temperatures)):
            while s and temperatures[i] > s[-1][0]:
                st , si = s.pop()
                res[si] = i - si
            s.append((temperatures[i], i))
        return res