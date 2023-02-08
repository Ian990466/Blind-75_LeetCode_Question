"""
Runtime 775 ms      Beats 61.6%
Memory 28.4 MB      Beats 69.11%
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, largest_sum = 0, -inf
        
        for element in nums:
            prefix = max(element + prefix, element)
            largest_sum = max(prefix, largest_sum)

        return largest_sum