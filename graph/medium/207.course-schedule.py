#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (36.62%)
# Total Accepted:    187.6K
# Total Submissions: 512.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        indegree = [0 for i in range(numCourses)]
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][1]] += 1
            if graph.__contains__(prerequisites[i][0]):
                graph[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                graph[prerequisites[i][0]] = [prerequisites[i][1]]
        for _ in range(numCourses):
            v = self.findIndegreeeZero(indegree)
            edges = graph.get(v, [])
            for w in range(len(edges)):
                indegree[edges[w]] -= 1
        return sum(indegree) == -1 * numCourses

    
    def findIndegreeeZero(self, indegree):
        loc = -1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                indegree[i] = -1
                loc = i
                break
        return loc


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(s.canFinish(numCourses=numCourses, prerequisites=prerequisites))
