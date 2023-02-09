"""
Runtime 101 ms      Beats 31.63%
Memory 14.3 MB      Beats 98.93%

Feb 09, 2023 22:15
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sub_min, sub_max = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            current_min = min(
                nums[i],
                min(nums[i] * sub_min, nums[i] * sub_max)
            )
            current_max = max(
                nums[i],
                max(nums[i] * sub_min, nums[i] * sub_max)
            )
            sub_min = current_min
            sub_max = current_max
            ans = max(ans, sub_max)
        return ans