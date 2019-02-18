#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
# https://leetcode.com/problems/car-fleet/description/
#
# algorithms
# Medium (38.13%)
# Total Accepted:    12K
# Total Submissions: 31.6K
# Testcase Example:  '12\n[10,8,0,5,3]\n[2,4,1,1,3]'
#
# N cars are going to the same destination along a one lane road.  The
# destination is target miles away.
# 
# Each car i has a constant speed speed[l] (in miles per hour), and initial
# position position[l] miles towards the target along the road.
# 
# A car can never pass another car ahead of it, but it can catch up to it, and
# drive bumper to bumper at the same speed.
# 
# The distance between these two cars is ignored - they are assumed to have the
# same position.
# 
# A car fleet is some non-empty set of cars driving at the same position and
# same speed.  Note that a single car is also a car fleet.
# 
# If a car catches up to a car fleet right at the destination point, it will
# still be considered as one car fleet.
# 
# 
# How many car fleets will arrive at the destination?
# 
# 
# 
# Example 1:
# 
# 
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by
# itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the
# answer is 3.
# 
# 
# 
# Note:
# 
# 
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[l] <= 10 ^ 6
# 0 <= position[l] < target
# All initial positions are different.
# 
# 
#
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 0:
            return 0
        car_teams = 1
        car_speed_map = {}
        for i in range(len(position)):
            car_speed_map[position[i]] = speed[i]
        position.sort(reverse=True)
        pre = 0
        for i in range(1, len(position)):
            car_pre = (target - position[pre]) / car_speed_map[position[pre]]
            car_now = (target - position[i]) / car_speed_map[position[i]]
            if car_pre >= car_now:
                continue
            else:
                car_teams += 1
                pre = i
        return car_teams


if __name__ == '__main__':
    s = Solution()
    target = 10
    position = [0,4,2]
    speedd = [2,1,3]
    print(s.carFleet(target=target, position=position, speed=speedd))
    

