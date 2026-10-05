class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        l = 0
        res = 0

        for i in range(len(s)):
            count[s[i]] += 1
            while count[s[i]] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)
        
        return res