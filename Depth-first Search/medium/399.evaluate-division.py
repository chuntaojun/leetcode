#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (46.64%)
# Total Accepted:    69.4K
# Total Submissions: 148.6K
# Testcase Example:  '[ ["a","b"],["b","c"] ]\n[2.0,3.0]\n[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]'
#
# 
# Equations are given in the format A / B = k, where  A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0. queries are:  a / c = ?,  b / a = ?, a / e =
# ?,  a / a = ?, x / x = ? . return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# 
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
# 基本解题思路=>转为有向带权图进行计算（点到点的经过的边）
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        self.graph = defaultdict(set)
        self.weight = defaultdict()
        for idx, equ in enumerate(equations):
            self.graph[equ[0]].add(equ[1])
            self.graph[equ[1]].add(equ[0])
            self.weight[tuple(equ)] = values[idx]
            self.weight[(equ[1], equ[0])] = 1 / values[idx]
        res = []
        for que in queries:
            t = self.dfs(start=que[0], end=que[1], visited=set())
            if t == 0:
                t = -1.0
            res.append(t)
        return res

    def dfs(self, start, end, visited):
        if (start, end) in self.weight:
            return self.weight[(start, end)]
        if start not in self.graph or end not in self.graph:
            return 0
        if start in visited:
            return 0
        visited.add(start)
        res = 0
        for tmp in self.graph[start]:
            res = (self.dfs(tmp, end, visited) * self.weight[(start, tmp)])
            if res != 0:
                self.weight[(start, end)] = res
                break
        visited.remove(start)
        return res


if __name__ == '__main__':
    s = Solution()
    equations = [["a","e"],["b","e"]]
    values = [4.0,3.0]
    queries = [["a","b"],["e","e"],["x","x"]]
    print(s.calcEquation(equations=equations, values=values, queries=queries))
