class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p = {}
        for i in range(len(nums)):
            if nums[i] in p:
                dis = i - p[nums[i]]
                if dis <= k:
                    return True
            p[nums[i]] = i
        return False
