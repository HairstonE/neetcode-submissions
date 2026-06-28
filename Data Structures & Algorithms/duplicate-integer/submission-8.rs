impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        if nums.len() == 0 {
            return false
        }
        let mut nums_ref = nums.clone();
        nums_ref.sort();
        
        for i in 0..nums_ref.len() - 1{
            if nums_ref[i] == nums_ref[i+1]{
                return true
            }
        }
        return false
    }
}
