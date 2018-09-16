"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
"""
import numpy as np


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        length = len(matrix[0])
        width = len(matrix)
        for i in range(width):
            for j in range(length):
                if (i == 0 and j == length - 1) or (i == width - 1 and j == 0):
                    break
                if matrix[i][j] == -1:
                    continue
                temp_i = i + 1
                for k in range(j + 1, length):
                    if temp_i <= width - 1:
                        if matrix[i][j] == matrix[temp_i][k]:
                            matrix[temp_i][k] = -1
                        else:
                            return False
                    temp_i += 1
                matrix[i][j] = -1
        for l in matrix:
            print l
        return True

    def fun(self, matrix):
        """

        :param matrix:
        :return:
        """
        length = len(matrix[0])
        width = len(matrix)
        for i in range(length):
            if i == length: break
            j = 1
            for k in range(i + 1, length):
                if j == width: break
                if matrix[0][i] == matrix[j][k]: matrix[j][k] = -1
                else:
                    return False
                j += 1
            matrix[0][i] = -1
        for i in range(1, width):
            if i == width: break
            j = i + 1
            for k in range(1, length):
                if j == width: break
                if matrix[i][0] == matrix[j][k]: matrix[j][k] = -1
                else:
                    return False
                j += 1
            matrix[i][0] = -1
        return True


if __name__ == '__main__':
    s = Solution()
    print np.array(s.fun([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
