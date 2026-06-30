impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut res: String = String::new();

        for s in strs{
            res.push_str(&s.len().to_string());
            res.push('#');
            res.push_str(&s);
        }
        return res
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut res = Vec::new();
    let bytes = s.as_bytes();
    let mut i = 0;
    while i < bytes.len() {
        // 1. scan from i to the next '#' — that span is the length text
        let mut j = i;
        while bytes[j] != b'#' {
            j += 1;
        }
        // 2. parse the length
        let len: usize = s[i..j].parse().unwrap();
        // 3. the string is the `len` bytes after the '#'
        let start = j + 1;
        res.push(s[start..start + len].to_string());
        // 4. jump past this chunk to the next length prefix
        i = start + len;
    }
    res
    }
}
