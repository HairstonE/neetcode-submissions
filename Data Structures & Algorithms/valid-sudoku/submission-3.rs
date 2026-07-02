impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut cols = vec![HashSet::new(); board.len()];
        let mut square: HashMap<(usize, usize), HashSet<char>> = HashMap::new();

        for i in 0..board.len(){
            let mut rows = HashSet::new();
            for j in 0..board.len(){
                let c = board[i][j];
                if c == '.' {
                    continue;
                }
                let in_row = rows.contains(&c);
                let in_col = cols[j].contains(&c);
                let in_sq = square.get(&(i / 3, j / 3))
                                  .map_or(false, |set| set.contains(&c));

                if in_row || in_col || in_sq {
                    return false;
                }
                rows.insert(c);
                cols[j].insert(c);
                square.entry((i / 3, j / 3))
                    .or_insert_with(HashSet::new)
                    .insert(c);
            }
        }
        true
    }
}
