#Search in Rotated Sorted Array-Leetcode #33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] == target:
                return mid
        
            if nums[left] <= nums[mid]:  # left half is sorted
                if nums[left]<= target <= nums[mid]:   # target in left half range?
                    right = mid-1
                else:
                    left = mid+1
            else:                         # right half is sorted
                if nums[mid]<= target <= nums[right]:   # target in right half range?
                    left = mid+1
                else:
                    right = mid-1
    
        return -1


        