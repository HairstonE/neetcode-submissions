impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, Vec<String>> = HashMap::new();

        for word in strs {
            let mut sorted_word_vec: Vec<_> = word.chars().collect();
            sorted_word_vec.sort();
            let sorted_word = sorted_word_vec.into_iter().collect();

            map.entry(sorted_word)
            .and_modify(|v| v.push(word.clone()))
            .or_insert(vec![word.clone()]);
        }

        let mut res = vec![];
        for val in map.values(){
            res.push(val.to_vec());
        }
        return res
    }
}
