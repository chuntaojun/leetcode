#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (33.97%)
# Total Accepted:    32.7K
# Total Submissions: 96K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# Note:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#
import sys   
sys.setrecursionlimit(1000000)

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = [[-1 for i in range(n)] for j in range(n)]
        for i in range(len(flights)):
            graph[flights[i][0]][flights[i][1]] = flights[i][2]
        self.ans = []
        self.dfs(graph=graph, x=src, step=0, dst=dst, cost=0)
        result = 10001
        for i in range(len(self.ans)):
            if self.ans[i][1] <= K:
                result = min(result, self.ans[i][0])
        return result if result != 10001 else -1
    
    def dfs(self, graph, x, step, dst, cost):
        for i in range(len(graph[x])):
            if graph[x][i] != -1:
                if i == dst:
                    self.ans.append([cost +graph[x][i], step])
                else:
                    t = graph[x][i]
                    graph[x][i] = -1
                    self.dfs(graph=graph, x=i, step=step + 1, dst=dst, cost=cost + graph[x][i])
                    graph[x][i] = t



if __name__ == '__main__':
    s = Solution()
    n = 5
    flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
    src = 0
    dst = 4
    K = 1
    print(s.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, K=K))
