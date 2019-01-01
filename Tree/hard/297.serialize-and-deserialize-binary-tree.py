#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (38.25%)
# Total Accepted:    146.3K
# Total Submissions: 382.3K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        q = []
        tmp = []
        q.append(root)
        if root is None:
            return '[null]'
        now_node_size = len(q)
        while (len(q) != 0):
            if now_node_size == 0:
                now_node_size = len(q)
            node = q.pop(0)
            now_node_size -= 1
            if node is not None:
                tmp.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                tmp.append('null')
        return '[' + ','.join(tmp) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data.replace('[', '').replace(']', '')
        values = [s.strip() for s in data.split(',')]
        print(values)
        if values[0] == 'null':
            return None
        root = TreeNode(int(values[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(values):
            node = nodeQueue[front]
            front = front + 1

            item = values[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(values):
                break

            item = values[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root
        

if __name__ == '__main__':
    s = Codec()
    t = "[1,2,3,null,null,4,5]"
    s.deserialize(data=t)
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
