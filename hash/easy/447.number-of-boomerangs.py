#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (48.78%)
# Total Accepted:    48.9K
# Total Submissions: 100.2K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
#
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        length = len(points)
        ans = 0
        for i in range(length):
            point_dist_map = defaultdict(int)
            for j in range(length):
                key = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                point_dist_map[key] += 1
            for _, v in point_dist_map.items():
                if v != 1:
                    ans += v * (v - 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    t = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    print(s.numberOfBoomerangs(points=t))
    
