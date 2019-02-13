/*
 * @lc app=leetcode id=922 lang=java
 *
 * [922] Sort Array By Parity II
 *
 * https://leetcode.com/problems/sort-array-by-parity-ii/description/
 *
 * algorithms
 * Easy (66.46%)
 * Total Accepted:    25.4K
 * Total Submissions: 38.2K
 * Testcase Example:  '[4,2,5,7]'
 *
 * Given an array A of non-negative integers, half of the integers in A are
 * odd, and half of the integers are even.
 * 
 * Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
 * even, i is even.
 * 
 * You may return any answer array that satisfies this condition.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [4,2,5,7]
 * Output: [4,5,2,7]
 * Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been
 * accepted.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 2 <= A.length <= 20000
 * A.length % 2 == 0
 * 0 <= A[i] <= 1000
 * 
 * 
 * 
 * 
 * 
 */

class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int point = 0;
        int evenIndex = 0;
        int oddIndex = 1;
        while (oddIndex < A.length && evenIndex < A.length) {
            if (judge(A[evenIndex], 0)) {
                evenIndex += 2;
                continue;
            }
            if (judge(A[oddIndex], 1)) {
                oddIndex += 2;
                continue;
            }
            if (!judge(A[evenIndex], 0)) {
                while (oddIndex < A.length && judge(A[oddIndex], 1)) {
                    oddIndex += 2;
                }
                int t = A[evenIndex];
                A[evenIndex] = A[oddIndex];
                A[oddIndex] = t;
                oddIndex += 2;
            } else if (!judge(A[oddIndex], 0)) {
                while (evenIndex < A.length && judge(A[evenIndex], 0)) {
                    evenIndex += 2;
                }
                int t = A[oddIndex];
                A[oddIndex] = A[evenIndex];
                A[evenIndex] = t;
                evenIndex += 2;
            }
        }
        return A;
    }

    public boolean judge(int a, int flag) {
        return (a + flag) % 2 == 0;
    }
}

class Solution2 {
    public int[] sortArrayByParityII(int[] A) {
        int point = 0;
        while (point < A.length) {
            if (judge(A[point], point % 2)) {
                point += 1;
            } else {
                int fast = point + 1;
                while (fast < A.length && judge(A[fast], 1 - point % 2)) {
                    fast += 2;
                }
                int t = A[point];
                A[point] = A[fast];
                A[fast] = t;
            }
        }
        return A;
    }

    public boolean judge(int a, int flag) {
        return (a + flag) % 2 == 0;
    }
}
