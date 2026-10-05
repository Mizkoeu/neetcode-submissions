class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        # brute force
        for i in range(len(height)):
            l_max = max(height[:i]) if i>0 else 0
            r_max = max(height[i+1:]) if i<len(height)-1 else 0
            h = min(l_max, r_max)
            area = h-height[i] if h>height[i] else 0
            total += area
        return total