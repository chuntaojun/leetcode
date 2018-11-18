#
# [891] Score After Flipping Matrix
#
# https://leetcode.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (67.03%)
# Total Accepted:    7.4K
# Total Submissions: 11.1K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# We have a two dimensional matrix A where each value is 0 or 1.
# 
# A move consists of choosing any row or column, and toggling each value in
# that row or column: changing all 0s to 1s, and all 1s to 0s.
# 
# After making any number of moves, every row of this matrix is interpreted as
# a binary number, and the score of the matrix is the sum of these numbers.
# 
# Return the highest possible score.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.
# 
# 
# 
#
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i][0] != 1:
                self.change(A, i=i, j=-1)
        tmp = len(A)
        for i in range(len(A[0])):
            zero_count = 0
            for j in range(len(A)):
                if A[j][i] == 0:
                    zero_count += 1
            if (zero_count * 2) > tmp:
                self.change(A, i=-1, j=i)
        ans = 0
        print(A)
        for i in range(len(A)):
            s = ''
            for j in range(len(A[0])):
                s += str(A[i][j])
            ans += int(s, 2)
        return ans
    
    def change(self, A, i, j):
        if j == -1:
            for k in range(len(A[i])):
                A[i][k] = 1 if A[i][k] == 0 else 0
        else:
            for k in range(len(A)):
                A[k][j] = 1 if A[k][j] == 0 else 0
