package medium

import (
	"fmt"
)


func removeDuplicates(nums []int) int {
    if len(nums) == 1 {
        return 1
    }
    a := 0
    b := 1
    n := 0
    times := 1
    length := len(nums)
    lengthC := length
    for {
        if b == length || a == length {
            break
        }
        if nums[a] == nums[b] {
            if times == 2 {
                n += 1
                nums = append(nums[:b], nums[b + 1:]...)
                length --
            } else {
                times += 1
                a ++
                b ++
            }
        } else if nums[a] != nums[b] {
            a ++
            b ++
            times = 1
        }
	}
    fmt.Printf("%#v", nums)
    return lengthC - n
}

func main()  {
    t := []int{0,1,1,1,1,2,3,3}
    removeDuplicates(t)
}