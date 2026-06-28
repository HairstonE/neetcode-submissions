impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut comps: HashMap<i32, i32> = HashMap::new();
        
        for i in 0..nums.len(){
            if comps.contains_key(&(target - nums[i])){
                return vec![comps[&(target - nums[i])], i.try_into().unwrap()]
            } else {
                comps.insert(nums[i], i.try_into().unwrap());
            }
        }
        return vec![]
    }
}
