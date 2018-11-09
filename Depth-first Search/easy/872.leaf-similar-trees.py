# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import reduce
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l_leaf = self.dfs(node=root1)
        r_leaf = self.dfs(node=root2)
        if len(l_leaf) != len(r_leaf):
            return False
        for i in range(len(l_leaf)):
            if l_leaf[i] != r_leaf[i]:
                return False
        return True
    
    def dfs(self, node):
        tmp = []
        if node is None:
            return tmp
        if node.left is None and node.right is None:
            tmp.append(node.val)
            return tmp
        tmp.extend(self.dfs(node=node.left))
        tmp.extend(self.dfs(node=node.right))
        return tmp
        