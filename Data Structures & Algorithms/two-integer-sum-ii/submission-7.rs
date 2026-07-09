impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0;
        let mut right = numbers.len() - 1;

        while left < right {
            if numbers[left] + numbers[right] == target{
                return vec![left as i32 + 1, right as i32 + 1];
            } else if numbers[left] + numbers[right] < target {
                left += 1
            } else {
                right -= 1 
            }
        }
        return vec![-1, -1]
    }
}
