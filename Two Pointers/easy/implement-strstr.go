package medium

func strStr(haystack string, needle string) int {
    if len(needle) == 0 {
        return 0
    }
    next := make([]int, len(needle))
    next[0] = -1
    k := -1
    for j := 0; j < len(needle) - 1; {
        if k == -1 || needle[k] == needle[j] {
            j ++
            k ++
            if needle[j] != needle[k] {
                next[j] = k
            } else {
                next[j] = next[k]
            }
        } else {
            k = next[k]
        }
    }
    a := 0
    b := 0
    for {
        if a >= len(haystack) || b >= len(needle) {
            break
        }
        if b == -1 || haystack[a] == needle[b] {
            a ++
            b ++
        } else {
            b = next[b]
        }
    }
    if b == len(needle) {
        return a - b
    }
    return -1
}
