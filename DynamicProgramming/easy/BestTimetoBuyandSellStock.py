"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an
algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(prices))]
        ans = 0
        for i in range(1, len(prices)):
            dp[i] = max(prices[i] - prices[i - 1] + dp[i - 1], 0)
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    test = [7, 1, 5, 3, 6, 4, 9, 3, 5, 7, 6]
    print s.maxProfit(test)
