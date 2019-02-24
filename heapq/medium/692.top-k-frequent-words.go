/*
 * @lc app=leetcode id=692 lang=golang
 *
 * [692] Top K Frequent Words
 *
 * https://leetcode.com/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (44.69%)
 * Total Accepted:    50.8K
 * Total Submissions: 113.6K
 * Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
 *
 * Given a non-empty list of words, return the k most frequent elements.
 * Your answer should be sorted by frequency from highest to lowest. If two
 * words have the same frequency, then the word with the lower alphabetical
 * order comes first.
 * 
 * Example 1:
 * 
 * Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * Output: ["i", "love"]
 * Explanation: "i" and "love" are the two most frequent words.
 * ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
 * "is"], k = 4
 * Output: ["the", "is", "sunny", "day"]
 * Explanation: "the", "is", "sunny" and "day" are the four most frequent
 * words,
 * ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
 * 
 * 
 * 
 * Note:
 * 
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Input words contain only lowercase letters.
 * 
 * 
 * 
 * Follow up:
 * 
 * Try to solve it in O(n log k) time and O(n) extra space.
 * 
 * 
 */
package Medium

import (
	"math"
	"strings"
)

type Heapq struct {
	size	int
	cap	int
	elements	[]*Node
	cmp func(a, b *Node, isEqual *bool) int
}

type Node struct {
	s	string
	freq	int
}

func NewHeapq(cap int, cmp func(a, b *Node, isEqual *bool) int) *Heapq {
	heapq := &Heapq{cap: cap + 1, size:0, elements:make([]*Node, cap + 1), cmp:cmp}
	heapq.elements[0] = &Node{freq:math.MaxInt32}
	return heapq
}

func cmp(a, b *Node, isEqual *bool) int {
	if b.freq == a.freq {
		return strings.Compare(a.s, b.s)
	}
	return b.freq - a.freq
}

func (h *Heapq)Push(node *Node) {
	h.size ++
	i := h.size
	isEqual := false
	for ; h.cmp(h.elements[i / 2], node, &isEqual) > 0; i /= 2 {
		h.elements[i] = h.elements[i / 2]
	}
	if isEqual {
		h.size --
	} else {
		h.elements[i] = node		
	}
}

func (h *Heapq)Pop() string {
	i := 1
	child := 0
	maxElement := h.elements[i]
	lastElement := h.elements[h.size]
	h.size --
	isEqual := false
	for ; i * 2 <= h.size; i = child {
		child = i * 2
		if h.cmp(h.elements[child], h.elements[child + 1], &isEqual) > 0 {
			child ++
		}
		if h.cmp(lastElement, h.elements[child], &isEqual) > 0 {
			h.elements[i] = h.elements[child]
		} else {
			break
		}
	}
	h.elements[i] = lastElement
	return maxElement.s
}

func topKFrequent(words []string, k int) []string {
	wordDict := make(map[string]int)
	for i := 0; i < len(words); i ++ {
		if _, ok := wordDict[words[i]]; ok {
			wordDict[words[i]] ++
		} else {
			wordDict[words[i]] = 1
		}
	}
	heapq := NewHeapq(len(wordDict), cmp)
	for k, v := range wordDict {
		heapq.Push(&Node{s:k,freq:v})
	}
	ans := make([]string, k)
	for i := 0; i < k; i ++ {
		ans[i] = heapq.Pop()
	}
	return ans
}