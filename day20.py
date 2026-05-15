# Minimum Window Substring-Leetcode#76
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        formed = 0  # how many chars satisfy need
        required = len(need)  # unique chars needed
        left = 0
        min_len = float('inf')
        result = ""

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                formed += 1
            
            while formed == required:  # window is valid, shrink
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return result