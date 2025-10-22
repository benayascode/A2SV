# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

func findDisappearedNumbers(nums []int) []int {
    out := make([]int, len(nums))
    var miss []int
    
    for _,i := range(nums){
        out[i-1] = i
    }
    for i := 0; i < len(out); i++{
        if out[i] == 0{
            miss = append(miss, i+1)
        }
    }
    return miss
}