"""
Runtime 1649 ms     Beats 46.97%
Memory 18.5 MB      Beats 35.18%

Mar 02, 2023 19:21
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        a, b, target = 0, 0, 0

        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                a, b, target = i + 1, len(nums) - 1, 0 - nums[i]
                while a < b:
                    if nums[a] + nums[b] == target:
                        res.append([nums[i], nums[a], nums[b]])
                        while a < b and nums[a] == nums[a+1]:
                            a += 1
                        while a < b and nums[b] == nums[b-1]:
                            b -= 1
                        a += 1
                        b -= 1
                    elif nums[a] + nums[b] < target:
                        a += 1
                    else:
                        b -= 1
        return res