#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (40.87%)
# Total Accepted:    20.2K
# Total Submissions: 49.3K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import defaultdict
        import heapq
        char_dic = defaultdict(int)
        for i in range(len(S)):
            char_dic[S[i]] += 1
        arr = [[-1 * item[1], item[0]] for item in sorted(char_dic.items(), key=lambda item: item[1], reverse=True)]
        if abs(arr[0][0]) > (len(S) + 1) / 2:
            return ""
        s = []
        heapq.heapify(arr)
        while len(arr) >= 2:
            t_1 = heapq.heappop(arr)
            t_2 = heapq.heappop(arr)
            s.append(t_1[1])
            s.append(t_2[1])
            if abs(t_1[0]) - 1 > 0:
                t_1[0] = -1 * (abs(t_1[0]) - 1)
                heapq.heappush(arr, t_1)
            if abs(t_2[0]) - 1 > 0:
                t_2[0] = -1 * (abs(t_2[0]) - 1)
                heapq.heappush(arr, t_2)
        if len(arr):
            s.append(heapq.heappop(arr)[1])
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    t_1 = "aaab"
    t = "ogccckcwmbmxtsbmozli"
    print(s.reorganizeString(S=t_1))
