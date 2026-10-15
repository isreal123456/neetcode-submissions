class Solution:
    def productExceptSelf(self, nums):
        r = []

        n = 1
        for i in range(len(nums)):
            r.append(n)
            n *= nums[i]
        n = 1
        for i in range(len(nums)-1,-1,-1):
            r[i] *= n
            n *= nums[i]
        return r