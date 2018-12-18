#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (33.95%)
# Total Accepted:    274.7K
# Total Submissions: 809.2K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        a = 0; b = 1
        while a < len(intervals):
            if b == len(intervals):
                a += 1
                b = a + 1
                continue
            t_1 = intervals[a]
            t_2 = intervals[b]
            if t_1.end >= t_2.start:
                intervals[a].end = max(t_1.end, t_2.end)
                intervals.pop(b)
            else:
                a += 1
                b += 1
        return intervals


if __name__ == '__main__':
    s = Solution()
    t = []
    s.merge(intervals=t)
