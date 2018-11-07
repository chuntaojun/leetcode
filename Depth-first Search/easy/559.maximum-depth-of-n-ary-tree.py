# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        """
        :type val
        :type children: list
        """
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        depth = 1
        root_chil = root.children
        if len(root_chil) == 0:
            return depth
        for i in range(len(root_chil)):
            depth = max(depth, 1 + self.dfs(node=root_chil[i]))
        return depth
    
    def dfs(self, node):
        chil = node.children
        if len(chil) == 0:
            return 1
        depth = 1
        for i in range(len(chil)):
            depth = max(depth, 1 + self.dfs(chil[i]))
        return depth
