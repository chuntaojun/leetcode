#
# [529] Minesweeper
#
# https://leetcode.com/problems/minesweeper/description/
#
# algorithms
# Medium (50.56%)
# Total Accepted:    24.8K
# Total Submissions: 49.1K
# Testcase Example:  '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n[3,0]'
#
# Let's play the minesweeper game (Wikipedia, online game)!
# 
# You are given a 2D char matrix representing the game board. 'M' represents an
# unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a
# revealed blank square that has no adjacent (above, below, left, right, and
# all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
# adjacent to this revealed square, and finally 'X' represents a revealed
# mine.
# 
# Now given the next click position (row and column indices) among all the
# unrevealed squares ('M' or 'E'), return the board after revealing this
# position according to the following rules:
# 
# 
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it
# to revealed blank ('B') and all of its adjacent unrevealed squares should be
# revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then
# change it to a digit ('1' to '8') representing the number of adjacent
# mines.
# Return the board when no more squares will be revealed.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# [['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'M', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'X', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also
# means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been
# revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For
# example, you don't need to reveal all the unrevealed mines when the game is
# over, consider any cases that you will win the game or flag any squares.
# 
# 
#
import sys

sys.setrecursionlimit(1000000)


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.width = len(board[0])
        self.heigh = len(board)
        if board[click[1]][click[0]] == 'M':
            board[click[1]][click[0]] = 'X'
        for i in range(self.heigh):
            for j in range(self.width):
                if board[i][j] == 'E':
                    self.dfs(board=board, x=j, y=i)
        return board
    
    def dfs(self, board, x, y):
        if board[y][x] != 'E':
            return
        self.mineNum(board=board, x=x, y=y)
        self.dfs(board=board, x=x - 1, y=y)
        self.dfs(board=board, x=x + 1, y=y)
        self.dfs(board=board, x=x, y=y - 1)
        self.dfs(board=board, x=x, y=y + 1)
    
    def mineNum(self, board, x, y):
        nums = 0
        if not self.judge_is_overflow(x, y):
            return
        if self.judge_is_overflow(x=x-1, y=y) and board[y][x - 1] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x+1, y=y) and board[y][x + 1] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x, y=y-1) and board[y - 1][x] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x-1, y=y+1) and board[y + 1][x] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x-1, y=y-1) and board[y - 1][x - 1] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x-1, y=y+1) and board[y - 1][x - 1] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x+1, y=y-1) and board[y - 1][x - 1] == 'M':
            nums += 1
        if self.judge_is_overflow(x=x+1, y=y+1) and board[y - 1][x - 1] == 'M':
            nums += 1
        if nums == 0:
            board[y][x] = 'B'
        else:
            board[y][x] = nums

    def judge_is_overflow(self, x, y):
        if x < 0 or x > self.width or y < 0 or y > self.heigh:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    s.updateBoard(board=board, click=click)
    
