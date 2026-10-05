class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in last_pos:
                l = max(last_pos[s[r]]+1, l)
            last_pos[s[r]] = r
            res = max(res, r-l+1)
        return res