class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        try:
            return nums.index(target)
        except ValueError:
            return(-1)