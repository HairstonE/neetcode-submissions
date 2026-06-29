impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counts = HashMap::new();
        for num in nums {
            counts.entry(num)
            .and_modify(|v| *v += 1)
            .or_insert(1);
        }
        let mut heap:BinaryHeap<(i32, i32)> = counts.into_iter()
        .map(|(k, v)| (v, k))
        .collect();
        let mut res = vec![];
        for i in 0..k {
            if let Some(largest) = heap.pop(){
                res.push(largest.1);
            }
        }
        res
    }
}
