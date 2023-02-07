"""
Runtime 589 ms      Beats 33.95%
Memory 28.9 MB      Beats 16.53%

Feb 07, 2023 17:10
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for element in nums:
            if element in h:
                return True
            else:
                h.add(element)