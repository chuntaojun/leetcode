#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (40.70%)
# Total Accepted:    198.1K
# Total Submissions: 486.7K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# 
#
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.sudo = {}
        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                if board[i][j] != '.':
                    if self.sudo.__contains__('H-' + str(i)):
                        if board[i][j] in self.sudo['H-' + str(i)]:
                            return False
                        self.sudo['H-' + str(i)].append(board[i][j])
                    else:
                        self.sudo['H-' + str(i)] = [board[i][j]]

                    if self.sudo.__contains__('L-' + str(j)):
                        if board[i][j] in self.sudo['L-' + str(j)]:
                            return False
                        self.sudo['L-' + str(j)].append(board[i][j])
                    else:
                        self.sudo['L-' + str(j)] = [board[i][j]]

                    g_n = 'G-' + self.gNum(i=i, j=j)
                    if self.sudo.__contains__(g_n):
                        if board[i][j] in self.sudo[g_n]:
                            return False
                        self.sudo[g_n].append(board[i][j])
                    else:
                        self.sudo[g_n] = [board[i][j]]
        return True
    
    def gNum(self, i, j):
        return str(3 * (int(i / 3) + 1) + int(j / 3) + 1)


if __name__ == '__main__':
    s = Solution()
    t = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
    print(s.isValidSudoku(board=t))
