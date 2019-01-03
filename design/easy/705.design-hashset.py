#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (46.98%)
# Total Accepted:    10.8K
# Total Submissions: 23K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
# 
# 
# 
# Example:
# 
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
# 
# 
#
class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[] for i in range(10001)]
    
    def hash_fun(self, key):
        return int(key % 10000)

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        loc = self.hash_fun(key=key)
        if self.contains(key=key):
            self.hash[loc].remove(key)
        self.hash[loc].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        loc = self.hash_fun(key=key)
        if self.contains(key=key):
            self.hash[loc].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        loc = self.hash_fun(key=key)
        return (key in self.hash[loc])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
