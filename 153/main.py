from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # for index, number in enumerate(nums):
        #     if index == 0:
        #         if nums[index + 1] > number and nums[-1] > number:
        #             return number
        #     else:
        #         if number < nums[0]:
        #             return number
        # binary search
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
