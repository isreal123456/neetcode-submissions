class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nu = sorted(nums)
        o = []
        for i in range(len(nu)):
            r, l = i + 1, len(nu) - 1
            while l > r:
                p = nu[i] +nu[r] + nu[l] 
                if p == 0:
                    if [nu[i], nu[r], nu[l]] not in o:
                        o.append([nu[i], nu[r], nu[l]])
                    r += 1
                    l -= 1

                elif p > 0:
                    l -= 1

                else:
                    r += 1
        

        return o
            