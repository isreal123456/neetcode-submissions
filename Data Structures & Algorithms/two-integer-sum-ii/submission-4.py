class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        o = []
        while l < r:
            j = numbers[l] + numbers[r]
            if j < target:
                l += 1
            elif j > target:
                r -= 1
            elif j == target:
                o.append(l+1)
                o.append(r+ 1)
                return o
