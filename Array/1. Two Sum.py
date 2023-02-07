"""
Runtime 53 ms    Beats 98.9%
Memory 25 MB     Beats 34.63%

Feb 03, 2023 17:21
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]