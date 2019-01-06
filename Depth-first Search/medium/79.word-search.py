#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (29.78%)
# Total Accepted:    234.7K
# Total Submissions: 787.9K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                s = []
                self.dfs(tmp=board, x=i, y=j, w=len(board[0]), h=len(board), s=s, loc=0)
                if ''.join(s).__contains__(word):
                    return True
        return False
    
    def dfs(self, tmp, x, y, w, h, s, loc):
        if ''.join(s).__contains__(self.word):
            return True
        if (x < 0 or x >= h) or (y < 0 or y >= w):
            return False
        if loc >= len(self.word):
            return True
        if self.word[loc] == tmp[x][y]:
            s.append(tmp[x][y])
            t = tmp[x][y]
            tmp[x][y] = '0'
            loc += 1
            if self.dfs(tmp=tmp, x=x, y=y + 1, w=len(tmp[0]), h=len(tmp), s=s, loc=loc) or \
                self.dfs(tmp=tmp, x=x + 1, y=y, w=len(tmp[0]), h=len(tmp), s=s, loc=loc) or \
                self.dfs(tmp=tmp, x=x, y=y - 1, w=len(tmp[0]), h=len(tmp), s=s, loc=loc) or \
                self.dfs(tmp=tmp, x=x - 1, y=y, w=len(tmp[0]), h=len(tmp), s=s, loc=loc):
                return True
            else:
                tmp[x][y] = t
                s.pop()
                loc -= 1
                return False
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A"]]
    word = "A"
    print(s.exist(board=board, word=word))
    
