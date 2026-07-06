impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let set: HashSet<i32> = HashSet::from_iter(nums);
        for num in &set {
            let mut cur = 0;
            let mut counter = *num;
            if !set.contains(&(counter - 1)) {
                while set.contains(&counter){
                    cur += 1;
                    counter += 1;
                }
                
            }
            res = res.max(cur);
        }
        res
    }
}
