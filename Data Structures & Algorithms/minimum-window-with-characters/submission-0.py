class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        min_len = float('inf')
        l, r, start = 0, 0, 0
        freq_map, window = Counter(t), Counter()

        while r < len(s):
            c = s[r]
            window[c] += 1
            while not(freq_map - window):
                cur_len = r-l+1
                if cur_len < min_len:
                    start = l
                    min_len = cur_len
                window[s[l]] -= 1
                l += 1
            r += 1

        return '' if min_len == float('inf') else s[start:start+min_len]

