/*
 * @lc app=leetcode id=703 lang=golang
 *
 * [703] Kth Largest Element in a Stream
 *
 * https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
 *
 * algorithms
 * Easy (41.42%)
 * Total Accepted:    14.5K
 * Total Submissions: 34.9K
 * Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
 *
 * Design a class to find the kth largest element in a stream. Note that it is
 * the kth largest element in the sorted order, not the kth distinct element.
 * 
 * Your KthLargest class will have a constructor which accepts an integer k and
 * an integer array nums, which contains initial elements from the stream. For
 * each call to the method KthLargest.add, return the element representing the
 * kth largest element in the stream.
 * 
 * Example:
 * 
 * 
 * int k = 3;
 * int[] arr = [4,5,8,2];
 * KthLargest kthLargest = new KthLargest(3, arr);
 * kthLargest.add(3);   // returns 4
 * kthLargest.add(5);   // returns 5
 * kthLargest.add(10);  // returns 5
 * kthLargest.add(9);   // returns 8
 * kthLargest.add(4);   // returns 8
 * 
 * 
 * Note: 
 * You may assume that nums' length ≥ k-1 and k ≥ 1.
 * 
 */
package easy

import (
	"fmt"
	"math"
	"testing"
)

type KthLargest struct {
	Priority	*Priority
	Kth	int
}

type Priority struct {
	Elements	[]int
	Size		int
}

func Constructor(k int, nums []int) KthLargest {
	p := &Priority{Elements: make([]int, k + 1, 2 * k), Size: 0}
	p.Elements[0] = -math.MaxInt32
	for i := range nums {
		if p.Size >= k && p.Elements[1] > nums[i] {
			continue
		}
		if p.Size >= k && p.Elements[1] < nums[i] {
			DeleteMin(p)
		}
		Insert(nums[i], p)
	}
	return KthLargest{Priority: p, Kth: k}
}

func Insert(value int, priority *Priority) {
	i := priority.Size + 1
	priority.Size += 1
	for ; priority.Elements[i / 2] > value; i = i / 2 {
		priority.Elements[i] = priority.Elements[i / 2]
	}
	priority.Elements[i] = value
}

func DeleteMin(priority *Priority) int {
	i := 1
	child := 0
	MinElement := priority.Elements[1]
	LastElement := priority.Elements[priority.Size]
	priority.Size -= 1
	for ; i * 2 <= priority.Size; i = child {
		child = i * 2
		if priority.Elements[child] > priority.Elements[child + 1] {
			child += 1
		}
		if LastElement > priority.Elements[child] {
			priority.Elements[i] = priority.Elements[child]
		} else {
			break
		}
	}
	priority.Elements[i] = LastElement
	return MinElement
}

func (this *KthLargest) Add(val int) int {
	if this.Priority.Size < this.Kth {
		Insert(val, this.Priority)
	} else if this.Priority.Elements[1] < val {
		DeleteMin(this.Priority)
		Insert(val, this.Priority)
	}
	return this.Priority.Elements[1]
}

func TestStream(t *testing.T)  {
	k := 3
	nums := []int{2,5,8,4}
	obj := Constructor(k, nums)
	fmt.Printf("%d\n", obj.Add(3))
	fmt.Printf("%d\n", obj.Add(5))
	fmt.Printf("%d\n", obj.Add(10))
	fmt.Printf("%d\n", obj.Add(9))
	fmt.Printf("%d\n", obj.Add(4))
}