class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        length = len(height)
        # make prefix max
        left_max, right_max = [0] * length, [0] * length
        left_max[0], right_max[-1] = height[0], height[-1]
        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(length-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        # brute force
        for i in range(len(height)):
            h = min(left_max[i], right_max[i])
            area = h-height[i] if h>height[i] else 0
            total += area
        return total