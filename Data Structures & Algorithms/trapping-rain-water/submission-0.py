class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        fmax = height[l]
        bmax = height[r]
        re =0
        while l<r:
            if fmax > bmax:
                r -= 1
                bmax = max(bmax, height[r])
                re += bmax - height[r]
            else:
                l += 1
                fmax = max(fmax, height[l])
                re += fmax - height[l]
        return re