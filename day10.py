#Product of Array Except Self-Leetcode#238
class Solution:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        right = [1] * len(nums)
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        answer = []
        for k in range(len(nums)):
            answer.append(left[k] * right[k])
        
        return answer