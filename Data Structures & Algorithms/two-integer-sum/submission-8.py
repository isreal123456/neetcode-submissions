class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        n = []
        for i in range(len(nums)):
            q = target - nums[i]
            if q in n:
                return[n.index(q), i]
            n.append(nums[i])
