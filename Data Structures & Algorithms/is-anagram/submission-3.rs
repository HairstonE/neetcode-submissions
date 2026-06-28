impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        //let mut anagrams = HashMap::new();
        let mut s_sort: Vec<char> = s.chars().collect();
        s_sort.sort();

        let mut t_sort: Vec<char> = t.chars().collect();
        t_sort.sort();
        
        s_sort == t_sort
    }
}
