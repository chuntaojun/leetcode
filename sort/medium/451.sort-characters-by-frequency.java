import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/*
 * @lc app=leetcode id=451 lang=java
 *
 * [451] Sort Characters By Frequency
 *
 * https://leetcode.com/problems/sort-characters-by-frequency/description/
 *
 * algorithms
 * Medium (54.30%)
 * Total Accepted:    78.3K
 * Total Submissions: 144.2K
 * Testcase Example:  '"tree"'
 *
 * Given a string, sort it in decreasing order based on the frequency of
 * characters.
 * 
 * Example 1:
 * 
 * Input:
 * "tree"
 * 
 * Output:
 * "eert"
 * 
 * Explanation:
 * 'e' appears twice while 'r' and 't' both appear once.
 * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
 * answer.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * "cccaaa"
 * 
 * Output:
 * "cccaaa"
 * 
 * Explanation:
 * Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
 * Note that "cacaca" is incorrect, as the same characters must be together.
 * 
 * 
 * 
 * Example 3:
 * 
 * Input:
 * "Aabb"
 * 
 * Output:
 * "bbAa"
 * 
 * Explanation:
 * "bbaA" is also a valid answer, but "Aabb" is incorrect.
 * Note that 'A' and 'a' are treated as two different characters.
 * 
 * 计数排序
 */


class Solution {
    public String frequencySort(String s) {
        TreeMap<Character, Integer> charMap = new TreeMap<>();

        Comparator<Map.Entry<Character, Integer>> valueComparator = (o1, o2) -> o2.getValue() - o1.getValue();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (charMap.containsKey(c)) {
                charMap.put(c, charMap.get(c) + 1);
            } else {
                charMap.put(c, 1);
            }
        }

        List<Map.Entry<Character, Integer>> list = new ArrayList<Map.Entry<Character,Integer>>(charMap.entrySet());

        Collections.sort(list, valueComparator);

        StringBuilder sb = new StringBuilder();

        for (Map.Entry<Character, Integer> entry : list) {
            for (int i = 0; i < entry.getValue(); i ++) {
                sb.append(entry.getKey());
            }
        }

        return sb.toString();

    }
}
