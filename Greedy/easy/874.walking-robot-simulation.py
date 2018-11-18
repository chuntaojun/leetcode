#
# [906] Walking Robot Simulation
#
# https://leetcode.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (28.43%)
# Total Accepted:    5.5K
# Total Submissions: 19.5K
# Testcase Example:  '[4,-1,3]\n[]'
#
# A robot on an infinite grid starts at point (0, 0) and faces north.  The
# robot can receive one of three possible types of commands:
# 
# 
# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# 
# 
# Some of the grid squares are obstacles. 
# 
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
# 
# If the robot would try to move onto them, the robot stays on the previous
# grid square instead (but still continues following the rest of the route.)
# 
# Return the square of the maximum Euclidean distance that the robot will be
# from the origin.
# 
# 
# 
# Example 1:
# 
# 
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# 
# 
# 
# Example 2:
# 
# 
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to
# (1, 8)
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# The answer is guaranteed to be less than 2 ^ 31.
# 
# 
#
from collections import defaultdict


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        com_left = -2; com_right = -1
        dir_l = 2; dir_r = -2; dir_up = 1; dir_down = -1
        pre_dir = dir_up
        x = 0; y = 0
        max_ans = 0
        obs = defaultdict(int)
        for item in obstacles:
            obs[(item[0], item[1])] = 1
        for comm in commands:
            if (comm == com_left and pre_dir == dir_up) or (comm == com_right and pre_dir == dir_down):
                pre_dir = dir_l
            elif (comm == com_left and pre_dir == dir_down) or (comm == com_right and pre_dir == dir_up):
                pre_dir = dir_r
            elif (comm == com_left and pre_dir == dir_l) or (comm == com_right and pre_dir == dir_r):
                pre_dir = dir_down
            elif (comm == com_left and pre_dir == dir_r) or (comm == com_right and pre_dir == dir_l):
                pre_dir = dir_up
            else:
                _x, _y = self.move_towards(dir=pre_dir)
                for _ in range(comm):
                    x += _x
                    y += _y
                    if obs[(x, y)] == 1:
                        print("遇到障碍物")
                        x -= _x
                        y -= _y
                        break
                    max_ans = max(self.cul(x=x, y=y), max_ans)
        return max_ans
        
    def cul(self, x, y):
        return x ** 2 + y ** 2
    
    def move_towards(self, dir):
        if dir == 2:
            return -1, 0
        if dir == -2:
            return 1, 0
        if dir == 1:
            return 0, 1
        if dir == -1:
            return 0, -1