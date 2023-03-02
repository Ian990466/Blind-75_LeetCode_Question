"""
Runtime 660 ms      Beats 97.8%
Memory 25.2 MB      Beats 99.93%

Mar 02, 2023 19:39
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        most, a , b = 0, 0, len(height)-1

        while a < b:
            buffer = 0
            if height[a] >= height[b]:
                buffer = height[b] * (b - a)
                b -= 1
            else:
                buffer = height[a] * (b - a)
                a += 1
            if buffer > most:
                print(a, b)
                most = buffer

        return most