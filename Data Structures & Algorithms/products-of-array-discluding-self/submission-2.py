class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, backward = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            forward[i] = nums[i-1] * forward[i-1]
        for j in range(len(nums)-2, -1, -1):
            backward[j] = nums[j+1] * backward[j+1]


        res = []
        for n in range(len(nums)):
            res.append(forward[n] * backward[n])
        
        return res