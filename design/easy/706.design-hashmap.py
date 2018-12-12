#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (51.05%)
# Total Accepted:    12.4K
# Total Submissions: 24.4K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value
# already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if
# this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the
# mapping for the key.
# 
# 
# 
# Example:
# 
# 
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 
# 
# 
# 
# Note:
# 
# 
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
# 
# 
#
class MyHashMap(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table_size = 32
        self.entry = [0 for i in range(32)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hash_code = self.hash(key=key)
        if self.entry[hash_code] != 0:
            is_append = True
            for i in self.entry[hash_code]:
                if i[0] == key:
                    is_append = False
                    i[1] = value
                    break
            if is_append:
                self.entry[hash_code].append([key, value])
        else:
            self.entry[hash_code] = [[key, value]]

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_code = self.hash(key=key)
        if self.entry[hash_code] != 0:
            for i, j in self.entry[hash_code]:
                if i == key:
                    return j
            return -1
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hash_code = self.hash(key=key)
        remove_target_value = None
        if self.entry[hash_code] != 0:
            for i, j in self.entry[hash_code]:
                if i == key:
                    remove_target_value = j
                    break
        if remove_target_value is not None and key is not None:
                self.entry[hash_code].remove([key, remove_target_value])
    
    def hash(self, key):
        t = str(key)
        hash_code = 0
        for i in range(len(t)):
            hash_code = (hash_code << 5) + int(t[i]) + 1
        return int(hash_code % self.table_size)



if __name__ == '__main__':
    myMap = MyHashMap()
    myMap.put(1, 1)
    myMap.put(2, 2)
    print(myMap.get(1))
    print(myMap.get(3))
    myMap.put(2, 1)
    print(myMap.get(2))
    myMap.remove(2)
    print(myMap.get(2))
