class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nu = []

        for x in nums:
            if x in nu:
                return True
            nu.append(x)

        return False
                