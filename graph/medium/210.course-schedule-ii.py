#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (33.60%)
# Total Accepted:    130.4K
# Total Submissions: 388K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
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
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        indegree = [0 for i in range(numCourses)]
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][1]] += 1
            if graph.__contains__(prerequisites[i][0]):
                graph[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                graph[prerequisites[i][0]] = [prerequisites[i][1]]
        ans = []
        for _ in range(numCourses):
            v = self.findIndegreeeZero(indegree)
            if v != -1:
                ans.append(v)
            edges = graph.get(v, [])
            for w in range(len(edges)):
                indegree[edges[w]] -= 1
        ans.reverse()
        return ans if sum(indegree) == -1 * numCourses else []

    
    def findIndegreeeZero(self, indegree):
        loc = -1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                indegree[i] = -1
                loc = i
                break
        return loc
