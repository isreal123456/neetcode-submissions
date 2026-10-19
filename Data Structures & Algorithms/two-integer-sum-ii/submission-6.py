class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers) - 1
        o = []
        while l < r:
            t = numbers[l] + numbers[r]
            if t > target:
                r -= 1
            if t < target:
                l += 1
            if t == target:
               return [l + 1, r + 1]