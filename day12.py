#Jump Game-Leetcode#55
class Solution:
    def canJump(self, nums):
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
        return True