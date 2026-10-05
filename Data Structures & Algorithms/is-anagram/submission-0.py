class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1

        if len(s_dict) != len(t_dict): return False
        for key in s_dict.keys():
            if key not in t_dict.keys():
                return False
            if s_dict[key] != t_dict[key]:
                return False
        return True
