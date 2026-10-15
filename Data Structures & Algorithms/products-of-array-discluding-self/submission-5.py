class Solution:
    def productExceptSelf(self, nums):
        r = [1] * len(nums)

        n = 1
        for i in range(len(nums)):
            r[i] = n
            n *= nums[i]
        n = 1
        for i in range(len(nums)-1,-1,-1):
            r[i] *= n
            n *= nums[i]
        return r