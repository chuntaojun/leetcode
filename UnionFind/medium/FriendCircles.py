"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we
defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        length = len(M)
        self.sign = [i for i in range(length)]
        for temp in range(len(M)):
            for a in range(len(M[temp])):
                if M[temp][a] == 1:
                    self.merge(temp, a)
        count = 0
        for i in range(len(self.sign)):
            if self.sign[i] == i:
                count += 1
        return count

    def find(self, x):
        """
        :param x:
        :param y:
        :return:
        """
        r = x
        while self.sign[r] != r:
            r = self.sign[r]
        return r

    def merge(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        _x = self.find(x)
        _y = self.find(y)
        if _x != _y:
            self.sign[_x] = _y


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
