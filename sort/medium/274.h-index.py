#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.39%)
# Total Accepted:    116.1K
# Total Submissions: 337.6K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        self.qSort(A=citations, start=0, end=len(citations) - 1)
        h = 0
        for i in range(len(citations)):
            if citations[i] != 0:
                if citations[i] > h:
                    h += 1
            else:
                break
        return h 
    
    def qSort(self, A, start, end):
        if start < end:
            i = start
            j = end
            key = A[(i + j) // 2]
            while i <= j:
                while A[i] > key:
                    i += 1
                while A[j] < key:
                    j -= 1
                if i <= j:
                    A[i], A[j] = A[j], A[i]
                    i += 1
                    j -= 1
            self.qSort(A=A, start=start, end=j)
            self.qSort(A=A, start=i, end=end)

if __name__ == '__main__':
    s = Solution()
    test = [3,0,6,1,5]
    print(s.hIndex(citations=test))
    
