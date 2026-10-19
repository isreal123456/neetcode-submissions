class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        o =[]
        nums.sort()
        for i in range(len(nums)):

            l = i + 1
            r = len(nums) - 1
            while l < r:
                n = nums[i] +nums[l] + nums[r]
                if n > 0:
                    r-=1
                elif n < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in o:
                        o.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
        return o