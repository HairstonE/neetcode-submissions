impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        //res[i] = nums[i] * trail[i-1], forward 
        let mut forward: Vec<i32> = vec![1; nums.len()];
        for i in 1..nums.len(){
            forward[i] = nums[i-1] * forward[i - 1]; 
        }

        let mut rev: Vec<i32> = vec![1; nums.len()];
        for i in (0..nums.len() - 1).rev(){
            rev[i] = nums[i+1] * rev[i + 1];
        }
        let mut res: Vec<i32> = vec![0; nums.len()];
        for i in 0..nums.len(){
            res[i] = forward[i] * rev[i];
        }

        res
    }
}
