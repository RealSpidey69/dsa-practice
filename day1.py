# Two Sum — LeetCode #1
# Given an array and target, return indices of two numbers that add to target

def twoSum(nums, target):
    for j in range(len(nums)):
        for i in range(j+1, len(nums)):
            if nums[j] + nums[i] == target:
                return j, i