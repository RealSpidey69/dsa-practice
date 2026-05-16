#Valid Anagram- Leetcode#242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        count_t={}
        for i in t:
                count_t[i]=count_t.get(i,0)+1
        return count_s==count_t
                