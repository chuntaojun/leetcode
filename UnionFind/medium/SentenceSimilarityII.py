"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar
word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good"
are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being
similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can
never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

"""


class Solution(object):
    def __init__(self):
        self.ans = {}
        self.temp = {}

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        cnt = 0
        for pair in pairs:
            for i in pair:
                if i not in self.temp:
                    self.temp[i] = cnt
                    cnt += 1
        self.adj = list(range(len(self.temp)))
        for i, j in pairs:
            self.union(self.temp[i], self.temp[j])
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] in self.temp and words2[i] in self.temp and self.find(self.temp[words1[i]]) == self.find(self.temp[words2[i]]):
                continue
            return False
        return True
        
    def find(self, i):
        while self.adj[i] != i:
            i = self.adj[i]
        return i

    def union(self, i, j):
        f1, f2 = self.find(i), self.find(j)
        self.adj[f1] = f2
