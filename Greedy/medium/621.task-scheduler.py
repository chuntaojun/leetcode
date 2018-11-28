#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (43.07%)
# Total Accepted:    58.1K
# Total Submissions: 134.8K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# 
# 
# Example:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# 
# Note:
# 
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        t_tasks = {}
        max_count = 0
        other_count = 0
        for i in tasks:
            if t_tasks.__contains__(i):
                t_tasks[i] += 1
            else:
                t_tasks[i] = 1
            max_count = max(max_count, t_tasks[i])
        for _, v in t_tasks.items():
            if v == max_count:
                other_count += 1
        return max(len(tasks), (max_count - 1) * (n + 1) + other_count)


if __name__ == '__main__':
    s = Solution()
    s.leastInterval(tasks=["A","A","A","B","B","B"], n=2)
    
