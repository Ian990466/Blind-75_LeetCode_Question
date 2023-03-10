"""
Runtime 43 ms       Beats 69.50%
Memory 14.3 MB      Beats 48.96%

Feb 13, 2023 02:42
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1