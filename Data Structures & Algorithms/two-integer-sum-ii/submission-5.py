class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        g = []
        while l <r:
            t = numbers[l] + numbers[r]
            if t > target:
                r -= 1
            if t < target:
                l += 1
            elif t == target:
                g.append(l + 1)
                g.append(r + 1)
                return g