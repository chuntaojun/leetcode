"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

this problem have use DP

"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, res = {}, 0
        for num in nums:
            if ans.has_key(num) is False:
                left = ans.get(num - 1) if ans.has_key(num - 1) else 0
                right = ans.get(num + 1) if ans.has_key(num + 1) else 0
                sums = left + right + 1
                ans[num] = sums
                res = max(res, sums)
                ans[num - left] = sums
                ans[num + right] = sums
            else:
                continue
        return res


if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
