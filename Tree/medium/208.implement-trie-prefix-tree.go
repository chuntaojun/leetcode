/*
 * @lc app=leetcode id=208 lang=golang
 *
 * [208] Implement Trie (Prefix Tree)
 *
 * https://leetcode.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (36.84%)
 * Total Accepted:    163.2K
 * Total Submissions: 442.9K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * Implement a trie with insert, search, and startsWith methods.
 *
 * Example:
 *
 *
 * Trie trie = new Trie();
 *
 * trie.insert("apple");
 * trie.search("apple");   // returns true
 * trie.search("app");     // returns false
 * trie.startsWith("app"); // returns true
 * trie.insert("app");
 * trie.search("app");     // returns true
 *
 *
 * Note:
 *
 *
 * You may assume that all inputs are consist of lowercase letters a-z.
 * All inputs are guaranteed to be non-empty strings.
 *
 * 前缀树
 */
package medium

type Trie struct {
	Root *TrieNode
}

type TrieNode struct {
	IsWord bool
	Childs []*TrieNode
}

func NewTrieNode() *TrieNode {
	node := &TrieNode{}
	node.IsWord = false
	node.Childs = make([]*TrieNode, 26)
	return node
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{Root: NewTrieNode()}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	p := this.Root
	words := []rune(word)
	for i := 0; i < len(words); i++ {
		loc := int(words[i]) - int('a')
		if p.Childs[loc] == nil {
			p.Childs[loc] = NewTrieNode()
		}
		p = p.Childs[loc]
	}
	p.IsWord = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	p := this.find(word)
	return p != nil && p.IsWord
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	return this.find(prefix) != nil
}

func (this *Trie) find(prefix string) *TrieNode {
	p := this.Root
	prefixChars := []rune(prefix)
	for i := 0; i < len(prefixChars); i++ {
		p = p.Childs[int(prefixChars[i])-int('a')]
		if p == nil {
			break
		}
	}
	return p
}
