from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        rot = left
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left <= right:
            mid = int((left + right) / 2)
            realmid = (mid + rot) % n
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    # left = abs(nums[0] - target)
    # right = abs(nums[-1] - target)
    # if left <= right:
    #     prev = nums[0]
    #     for index, number in enumerate(nums):
    #         if number == target:
    #             return index
    #         elif number < prev:
    #             return -1
    #         prev = number
    #     return -1
    # else:
    #     prev = nums[-1]
    #     for i in range(len(nums) - 1, -1, -1):
    #         if nums[i] == target:
    #             return i
    #         elif prev < nums[i]:
    #             return -1
    #         prev = nums[i]
    #     return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8))
