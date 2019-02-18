#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (70.82%)
# Total Accepted:    58.5K
# Total Submissions: 82.6K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
# 
# 
#
# Definition for a binary tree node.
import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(nums=nums, start=0, end=len(nums) - 1)

    def buildTree(self, nums, start, end):
        if start > end:
            return None
        else:
            maxN, loc = self.findMax(arr=nums, start=start, end=end)
            root = TreeNode(maxN)
            root.left = self.buildTree(nums=nums, start=start, end=loc-1)
            root.right = self.buildTree(nums=nums, start=loc + 1, end=end)
            return root
    
    def findMax(self, arr, start, end):
        index = 0
        n = -1
        for i in range(start, end + 1):
            if arr[i] > n:
                n = arr[i]
                index = i
        return n, index

def stringToIntegerList(input):
    return json.loads(input)

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().constructMaximumBinaryTree(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
        
