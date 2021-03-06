#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (56.57%)
# Total Accepted:    37.2K
# Total Submissions: 65.8K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0 for i in T]
        tmp = []
        for i in range(len(T)):
            if len(tmp) == 0:
                tmp.insert(0, {"index": i, "tmp": T[i]})
                continue
            if T[i] <= tmp[0]["tmp"]:
                tmp.insert(0, {"index": i, "tmp": T[i]})
            else:
                while len(tmp) != 0 and T[i] > tmp[0]["tmp"]:
                    item = tmp[0]
                    tmp.remove(item)
                    ans[item["index"]] = i - item["index"]
                tmp.insert(0, {"index": i, "tmp": T[i]})
        return ans


if __name__ == '__main__':
    s = Solution()
    s.dailyTemperatures(T=[73,74,75,71,69,72,76,73])
    
