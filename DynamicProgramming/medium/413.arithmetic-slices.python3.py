#
# [413] Arithmetic Slices
#
# https://leetcode-cn.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (51.96%)
# Total Accepted:    1.4K
# Total Submissions: 2.7K
# Testcase Example:  '[1,2,3,4]'
#
# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 
# 例如，以下数列为等差数列:
# 
# 
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# 以下数列不是等差数列。
# 
# 
# 1, 1, 2, 5, 7
# 
# 
# 
# 数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
# 
# 如果满足以下条件，则称子数组(P, Q)为等差数组：
# 
# 元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。
# 
# 函数要返回数组 A 中所有为等差数组的子数组个数。
# 
# 
# 
# 示例:
# 
# 
# A = [1, 2, 3, 4]
# 
# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
# 
# 
# 还不是最优解
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        if len_a <= 2:
            return 0
        dp = [[False for i in range(len_a)] for j in range(len_a)]
        tmp = A[1] - A[0]; dp[0][1] = True
        loc = 0
        for i in range(2, len_a):
            if A[i] - A[i - 1] == tmp and dp[loc][i - 1]:
                for k in range(loc, i + 1):
                    dp[k][i] = True
            else:
                tmp = A[i] - A[i - 1]
                dp[loc][i] = False
                if i + 1 >= len_a:
                    break
                loc = i - 1
                dp[loc][i] = True
        # for i in range(len_a):
        #     print(dp[i])
        count = 0
        for i in range(len_a):
            loc = i
            for j in range(i + 2, len_a):
                if dp[loc][j]:
                    count += 1
                else:
                    break
        return count
    
