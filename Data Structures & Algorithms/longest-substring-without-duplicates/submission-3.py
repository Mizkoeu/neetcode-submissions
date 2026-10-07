class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1: return len(s)
        longest = 1
        seen = {} 
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]]+1)
            longest = max(longest, r-l+1)
            seen[s[r]] = r
            r+=1

        return longest
            