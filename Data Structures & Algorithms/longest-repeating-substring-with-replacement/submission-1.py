class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        counts = Counter()
        result = 0

        for i in range(len(s)):
            counts[s[i]] += 1
            max_freq = counts.most_common(1)[0][1]
            while left < i:
                if i - left + 1 - max_freq <= k:
                    result = max(result, i-left+1)
                    break
                else:
                    counts[s[left]] -= 1
                    left += 1
        return result