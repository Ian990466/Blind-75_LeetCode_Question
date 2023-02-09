"""
Runtime 43 ms       Beats 67.97%
Memory 14.1 MB      Beats 93.95%

Feb 09, 2023 22:59
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[-1] > nums[0]:
            return nums[0]
    
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]