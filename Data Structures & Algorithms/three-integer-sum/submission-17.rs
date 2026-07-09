impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        let mut sorted = nums.clone();
        sorted.sort();
        

        for (mut i) in 0..sorted.len() {
            if i > 0 && sorted[i] == sorted[i - 1]{
                continue;
            }
            let mut j = i + 1;
            let mut k = sorted.len() - 1;
            while j < k {
                let sum = sorted[i] + sorted[j] + sorted[k];
                if sum == 0 {
                    res.push(vec![sorted[i], sorted[j], sorted[k]]);
                    j += 1;
                    while j < k && k < sorted.len() && sorted[j] == sorted[j - 1]{
                        j += 1;
                    }
                } else if sum > 0 {
                    k -= 1;
                    while j < k && k < sorted.len() - 1 && sorted[k] == sorted[k + 1]{
                        k -= 1;
                    }
                } else {    
                    j += 1;
                }
            }
        }
        res
    }
}
