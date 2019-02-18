#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (37.61%)
# Total Accepted:    19.6K
# Total Submissions: 52.1K
# Testcase Example:  '[5,10,-5]'
#
# 
# We are given an array asteroids of integers representing asteroids in a row.
# 
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions.  If two asteroids
# meet, the smaller one will explode.  If both are the same size, both will
# explode.  Two asteroids moving in the same direction will never meet.
# 
# 
# Example 1:
# 
# Input: 
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation: 
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
# 
# 
# 
# Example 2:
# 
# Input: 
# asteroids = [8, -8]
# Output: []
# Explanation: 
# The 8 and -8 collide exploding each other.
# 
# 
# 
# Example 3:
# 
# Input: 
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation: 
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in
# 10.
# 
# 
# 
# Example 4:
# 
# Input: 
# asteroids = [-2, -1, 1, 2]
# Output: [-2, -1, 1, 2]
# Explanation: 
# The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet
# each other.
# 
# 
# 
# Note:
# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..
# 
#
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) == 0:
            return []
        plant_stack = []
        for i in range(0, len(asteroids)):
            if len(plant_stack) == 0:
                plant_stack.append(asteroids[i])
                continue
            if asteroids[i] < 0 and plant_stack[-1] > 0:
                while True:
                    m, r = self.crash_result(asteroids[i], plant_stack[-1])
                    if r < 0:
                        plant_stack.pop()
                        if len(plant_stack) == 0:
                            plant_stack.append(asteroids[i])
                            break
                    elif r == 0:
                        plant_stack.pop()
                        break
                    elif r == 1 and m:
                        plant_stack.append(asteroids[i])
                        break
                    else:
                        break
            else:
                plant_stack.append(asteroids[i])
        return plant_stack

        
    def crash_result(self, a, b):
        if a * b > 0:
            return True, 1
        return False, a + b

class Solution2:
    def asteroidCollision(self, asteroids):
        """
        双指针解决方案
        :type asteroids: List[int]
        :rtype: List[int]
        """
        pass


if __name__ == '__main__':
    s = Solution()
    n = [-2,-2,2,-1]
    print(s.asteroidCollision(asteroids=n))
    
