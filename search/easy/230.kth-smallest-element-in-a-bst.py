#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (48.63%)
# Total Accepted:    184.3K
# Total Submissions: 379K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        中序遍历，记录节点数目何时到达k
        """
        self.k = k
        self.t = 0
        return self.findKthMin(root=root)
    
    def findKthMin(self, root):
        if root == None:
            return 0
        left = self.findKthMin(root=root.left)
        if self.t == self.k:
            return left
        self.t += 1
        if self.t == self.k:
            return root.val
        return self.findKthMin(root=root.right)

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
            k = int(line);
            
            ret = Solution().kthSmallest(root, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()