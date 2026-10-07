class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        n = []
        for i in range(len(nums)):
            o = target - nums[i]
            if o in n:
                return [n.index(o), i]
            n.append(nums[i])