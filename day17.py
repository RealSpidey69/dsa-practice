#Valid Palindrome- Leetcode#125
class Solution:
    def isPalindrome(self, s):
        str = s.lower()
        new_s = ""
        for c in str:
            if c.isalnum():
                new_s += c
        rev = new_s[::-1]
        return new_s == rev
        