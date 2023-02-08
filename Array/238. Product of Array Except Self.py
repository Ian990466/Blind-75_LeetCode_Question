"""
Runtime 234 ms      Beats 82.71%
Memory 21.2 MB      Beats 69.17%

Feb 09, 2023 00:04
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, ans, pre_prod, suff_prod = len(nums), [1]*len(nums), 1, 1
            
        for i in range(n):
            #Prefix
            ans[i] *= pre_prod
            pre_prod *= nums[i]
            
            # Suffix
            ans[-1-i] *= suff_prod
            suff_prod *= nums[-1-i]
        
        return ans