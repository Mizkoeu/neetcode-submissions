class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # this is nlogn already
        result = []
        for i in range(len(nums) - 2):
            # now we want to find sum of -i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = -nums[i]
                sum = nums[l] + nums[r]
                if sum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif sum > target:
                    r -= 1
                else:
                    l += 1
        return result
