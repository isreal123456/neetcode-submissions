class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        g = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i +1
            r = len(nums) - 1
            while l < r:
                t = nums[i] +nums[l]+nums[r]
                if t < 0 :
                    l += 1
                elif t > 0:
                    r -= 1
                elif  t == 0:
                    g.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return g