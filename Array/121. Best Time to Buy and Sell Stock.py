"""
Runtime 917 ms      Beats 98.66%
Memory 25 MB        Beats 83.76%

Feb 07, 2023 16:57
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit