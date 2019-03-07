#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (36.84%)
# Total Accepted:    163.2K
# Total Submissions: 442.9K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
# 前缀树
class TrieNode(object):

    def __init__(self):
        self.isWord = False
        self.child = [None for _ in range(26)]

class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if p.child[index] is None:
                p.child[index] = TrieNode()
            p = p.child[index]
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.find(prefix=word)
        return p != None and p.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix=prefix) != None
    
    def find(self, prefix):
        p = self.root
        for i in range(len(prefix)):
            p = p.child[ord(prefix[i]) - ord('a')]
            if p == None:
                break
        return p
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
