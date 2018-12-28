#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.44%)
# Total Accepted:    33.4K
# Total Submissions: 75.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        width = len(matrix[0])
        height = len(matrix)
        if width == 1:
            return [matrix[i][0] for i in range(len(matrix))]
        edge = [i for i in range(width)]
        for i in range(2, height + 1):
            edge.append((width) * i - 1)
        edge_2 = [width * i for i in range(0, height)]
        for i in range(width):
            edge_2.append(edge_2[-1] + 1)
        print(edge_2)
        ans = [matrix[0][0]]
        for i in range(1, len(edge) - 1):
            tmp = []
            for j in range(edge[i], edge_2[i] + 1, width - 1):
                x, y = self.getLoc(n=j, width=width, height=height)
                if x < width and y < height:
                    tmp.append(matrix[y][x])
                else:
                    break
            if int(i % 2) == 0:
                tmp.reverse()
            ans.extend(tmp)
        ans.append(matrix[-1][-1])
        return ans

    def getLoc(self, n, width, height):
        x = int(n % width)
        y = int(n / width)
        return x, y


if __name__ == '__main__':
    s = Solution()
    t_1 = [[2,5],[8,4],[0,-1]]
    t = [[1,2,3,4,5,6,7],
         [8,9,10,11,12,13,14],
         [15,16,17,18,19,20,21]]
    print(s.findDiagonalOrder(matrix=t_1))
