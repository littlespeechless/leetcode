from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate left side and right product of a giving number
        # ex [1, 2, 3, 4] =
        # left = [1, 1, 2, 6]
        # right = [24, 12, 4, 1]
        solution = []
        temp = 0
        length = len(nums) - 1
        for index, value in enumerate(nums):
            if index == 0:
                solution.append(1)
            else:
                solution.append(solution[index - 1] * nums[index - 1])
        for index in range(length, -1, -1):
            if index == length:
                temp = 1
                solution[index] *= temp
            else:
                temp *= nums[index + 1]
                solution[index] *= temp
        # one loop
        """
        arr = [1] * len(nums)
        pi = pj = 1

        for i in range(len(nums)):
            j = -1-i
            arr[i]*=pi
            arr[j]*=pj
            pi *= nums[i]
            pj *= nums[j]        
                    
        return arr
        """
        return solution


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
