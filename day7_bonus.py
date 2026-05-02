#Maximum Subarray-Leetcode #53
class Solution:
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum