#
# @lc app=leetcode id=881 lang=python
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (41.01%)
# Total Accepted:    9.1K
# Total Submissions: 22.1K
# Testcase Example:  '[1,2]\n3'
#
# The i-th person has weight people[i], and each boat can carry a maximum
# weight of limit.
# 
# Each boat carries at most 2 people at the same time, provided the sum of the
# weight of those people is at most limit.
# 
# Return the minimum number of boats to carry every given person.  (It is
# guaranteed each person can be carried by a boat.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# 
# 
# 
# Example 2:
# 
# 
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# 
# 
# 
# Example 3:
# 
# 
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# 
# Note:
# 
# 
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000
# 
# 
# 
# 
# 
#
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0
        r = len(people) - 1
        total = 0
        nums = 2
        diff = limit - people[l]
        while l <= r and:
            if diff >= people[r]:
                total += 1
                people.remove(people[r])
                l += 1
                r = len(people) - 1
                if l >= len(people):
                    break
                diff = limit - people[l]
            else:
                r -= 1
        return total


if __name__ == '__main__':
    s = Solution()
    people = [1,1,1,2]
    limit = 3
    print(s.numRescueBoats(people=people, limit=limit))
