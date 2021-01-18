from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             # replace row to True
        #             for k in range(n):
        #                 if matrix[i][k] != 0:
        #                     matrix[i][k] = True
        #             for k in range(m):
        #                 if matrix[k][j] != 0:
        #                     matrix[k][j] = True
        #             continue
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] is True:
        #             matrix[i][j] = 0

        m = len(matrix)
        n = len(matrix[0])
        # overlapping position variable
        is_row = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        is_row = True
        # skip first row and col because they are our counter
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # clear first col
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        # clear fist row
        if is_row:
            for i in range(n):
                matrix[0][i] = 0

        return matrix


if __name__ == '__main__':
    print(Solution().setZeroes([[1,0,3]]))
