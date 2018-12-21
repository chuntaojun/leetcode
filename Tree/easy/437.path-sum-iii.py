#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (41.13%)
# Total Accepted:    83.3K
# Total Submissions: 202.4K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.roads = 0
        self.target = target
        self.preOrder(root=root)
        return self.roads
    
    def preOrder(self, root):
        if root != None:
            self.culPreOrder(root=root, k=0)
            self.preOrder(root=root.left)
            self.preOrder(root=root.right)
    
    def culPreOrder(self, root, k):
        if root != None:
            k = root.val + k
            if k == self.target:
                self.roads += 1
            self.culPreOrder(root=root.left, k=k)
            self.culPreOrder(root=root.right, k=k)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

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
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);
            
            ret = Solution().pathSum(root, sum)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()