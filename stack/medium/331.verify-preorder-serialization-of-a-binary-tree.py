#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (37.85%)
# Total Accepted:    53.1K
# Total Submissions: 140.2K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
# 
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# 
# 
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# 
# Input: "1,#"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: "9,#,#,1"
# Output: false
#
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder) == 1 and preorder[-1] == '#':
            return True
        preorder = preorder.split(',')
        c = 0
        while len(preorder) and preorder[-1] == '#':
            c += 1
            if c > 2:
                c -= 1
                break
            preorder.pop()
        if c != 2 or len(preorder) == 0:
            return False
        tree_node_stack = []
        for i in range(len(preorder)):
            if preorder[i] == '#':
                if len(tree_node_stack):
                    tree_node_stack.pop()
                else:
                    return False
            else:
                tree_node_stack.append(preorder[i])
        return len(tree_node_stack) >= 0


if __name__ == '__main__':
    s = Solution()
    t = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print(s.isValidSerialization(preorder=t))
    
