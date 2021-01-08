from typing import List, Dict


class Solution:
    # def twoSum(self, nums: Dict, target: int, ) -> List[List[int]]:
    #     keys = list(nums.keys())
    #     solution = []
    #     for index, number in enumerate(keys):
    #         gap = target - number
    #         temp = nums.pop(number)
    #         if len(temp) > 1:
    #             temp2 = temp.copy()
    #             temp2.pop()
    #             nums[number] = temp2
    #         if gap in nums.keys():
    #             solution.append([number, gap])
    #         nums[number] = temp
    #     return solution
    #
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 0:
    #         return []
    #     solution = set()
    #     indexing_dic = {}
    #     for index, number in enumerate(nums):
    #         if number in indexing_dic:
    #             indexing_dic[number].append(index)
    #         else:
    #             indexing_dic[number] = [index]
    #     for index, number in enumerate(nums):
    #         gap = 0 - number
    #         temp = indexing_dic.pop(number)
    #         if len(temp) > 1:
    #             temp2 = temp.copy()
    #             temp2.remove(index)
    #             indexing_dic[number] = temp2
    #         two_sum = self.twoSum(indexing_dic, gap)
    #         if len(two_sum) > 0:
    #             for i in two_sum:
    #                 i.append(number)
    #                 i.sort()
    #                 solution.add(tuple(i))
    #         indexing_dic[number] = temp
    #     solution = list(map(list, solution))
    #     return solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using two sum II solution (two pointer left and right)
        res = []
        # sort the list so avoid duplicate
        nums.sort()
        for i in range(len(nums) - 2):
            # skip duplicate as it will return duplicate solution
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # left and right pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # shift the point to left if sum is bigger than 0, and to the right if is less than right
                # because the list is being sorted move left pointer = increase, move right pointer = decrease
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    # case find solution
                    res.append([nums[i], nums[l], nums[r]])
                    # update pointer for two sum such that left pinter and right pointer skips duplicate number
                    # while l < r and nums[l] == nums[l + 1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r - 1]:
                    #     r -= 1
                    # l += 1
                    # r -= 1
                    # or better way, only update the left since right pointer will be taking care by finding two sum
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
