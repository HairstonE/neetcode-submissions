impl Solution {
    pub fn is_palindrome(s: String) -> bool {

        let mut word: Vec<char> = s.chars().collect();
        word.retain(|c| c.is_ascii_alphanumeric());
        if word.len() < 2 {return true}
        let mut i = 0;
        let mut j = word.len() - 1;
        while i <= j {
            let c1 = word[i].to_ascii_lowercase();
            let c2 = word[j].to_ascii_lowercase();
            if  c1 != c2 {
                return false
            }
            i += 1;
            j -= 1;
        }
        true
    }
}
