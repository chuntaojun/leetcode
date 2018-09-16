# -*- coding: UTF-8 -*-


"""Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the
maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(map(int, str(num)))
        length = len(num)
        max_num, max_loc = -1, 0
        for i in range(length):
            for j in range(i + 1, length, 1):
                if num[j] >= max_num:
                    max_loc = j
                    max_num = num[j]
            if num[i] < max_num:
                num[max_loc] = num[i]
                num[i] = max_num
                break
            max_num, max_loc = 0, 0
        return int("".join(map(str, num)))


if __name__ == '__main__':
    s = Solution()
    print s.maximumSwap(9973)
