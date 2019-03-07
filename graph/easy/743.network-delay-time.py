#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Easy (38.37%)
# Total Accepted:    19.1K
# Total Submissions: 49.9K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K.  How long will it take for all
# nodes to receive the signal?  If it is impossible, return -1.
# 
# 
# Note:
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1  and 1 .
# 
# 
#
import sys


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        self.graph = [[-1 for i in range(N)] for j in range(N)]
        self.point = [sys.maxsize if i != K - 1 else 0 for i in range(N)]
        for i in range(len(times)):
            self.graph[times[i][0] - 1][times[i][1] - 1] = times[i][2]
        self.q = [K]
        while len(self.q) != 0:
            _t = []
            for _ in range(len(self.q), 0, -1):
                t = self.q.pop(0)
                for i in range(N):
                    if self.graph[t - 1][i] != -1 and self.graph[t - 1][i] + self.point[t - 1] < self.point[i]:
                        if i not in _t:
                            _t.append(i)
                            self.q.append(i + 1)
                        self.point[i] = self.graph[t - 1][i] + self.point[t - 1]
        res = 0
        for i in range(N):
            res = max(res, self.point[i])
        return -1 if res == sys.maxsize else res


if __name__ == '__main__':
    s = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    print(s.networkDelayTime(times=times, N=N, K=K))
