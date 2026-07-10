impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut res = 0;

        let mut l = 0;
        let mut r = heights.len() - 1;

        while l < r {
            res = res.max(heights[l].min(heights[r]) * (r - l) as i32);
            if heights[l] <= heights[r]{
                l += 1;
            } else {
                r -= 1;
            }
        }
        res
    }
}
