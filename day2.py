#Palindrome Number-Leetcode#9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False 
        sum=0 
        num=x 
        while (num>0): 
            sum=sum*10+(num%10) 
            num=num//10
        if(sum==x):
            return True 
        return False
                