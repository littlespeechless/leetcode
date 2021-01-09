from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        current_max = 0
        # use two pointer and move the small pointer towards center at once
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            current_max = max(current_max, area)

        return current_max


if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
