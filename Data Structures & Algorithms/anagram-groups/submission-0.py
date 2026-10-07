class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            # letter freq array
            freq = [0 for _ in range(26)]
            for l in str:
                # convert letter into int
                freq[ord(l)-ord('a')] += 1
            count = tuple(freq)
            if count in res.keys():
                res[count].append(str)
            else:
                res[count] = [str]
        return [v for k, v in res.items()]
