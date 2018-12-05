# -*- coding: UTF-8 -*-


"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution(object):
    def __init__(self):
        self.queue = []

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        self.m, self.n = len(board), len(board[0])
        for i in range(self.n):
            self.BFS(board, 0, i)
            self.BFS(board, self.m - 1, i)
        for j in range(1, self.m - 1):
            self.BFS(board, j, 0)
            self.BFS(board, j, self.n - 1)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        print(board)

    def BFS(self, board, x, y):
        if board[x][y] == 'O':
            self.queue.append((x, y))
            self.fill(board, x, y)
        while self.queue:
            curr = self.queue.pop(0)
            i, j = curr[0], curr[1]
            self.fill(board, i + 1, j)
            self.fill(board, i - 1, j)
            self.fill(board, i, j - 1)
            self.fill(board, i, j + 1)

    def fill(self, board, x, y):
        """
        广度优先遍历搜索的路径实现
        :param board:
        :param x:
        :param y:
        :return:
        """
        if x < 0 or x > self.m - 1 or y < 0 or y > self.n - 1 or board[x][y] != 'O':
            return
        self.queue.append((x, y))
        board[x][y] = 'D'


if __name__ == '__main__':
    s = Solution()
    s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "O", "X", "X"]])
