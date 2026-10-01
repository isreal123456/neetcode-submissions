class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i =Counter(nums)

        for x, num in i.items():

            if num > 1:
                return True
            

        return False
                