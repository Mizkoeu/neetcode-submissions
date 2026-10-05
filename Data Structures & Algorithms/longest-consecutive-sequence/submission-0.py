class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set()
        for num in nums:
            elements.add(num)

        max_count = 0

        for num in nums:
            if num-1 not in elements:
                count = 1
                next = num+1
                while next in elements:
                    count+=1
                    next+=1
                max_count = max(max_count, count)
        
        return max_count