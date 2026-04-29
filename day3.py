#Roman to Integer-Leetcode#13
class Solution:
    def romanToInt(self, s: str) -> int:
        values = { 'I': 1, 'IV': 4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D': 500, 'CM':900, 'M': 1000 } 
        a=len(s)
        i=0 
        sum=0
        while(i<a): 
            if(s[i:i+2] in values): 
                        sum+=values[s[i:i+2]]
                        i+=2 
            else: 
                        sum+=values[s[i]]
                        i+=1
        return sum