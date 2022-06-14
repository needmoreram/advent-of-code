use std::fs;
use std::error::Error;

struct BingoBoard {
  values: [[i32; 5]; 5],
}

impl BingoBoard {
  fn cross_out(&self, called: i32) {
  }

  fn won(&self) -> bool {
    false
  }
}

fn main() {
  let contents = fs::read_to_string("input/day-4.txt").expect("error!");
  let blocks: Vec<&str> = contents.split("\n\n").collect();

  let mut boards: Vec<BingoBoard> = Vec::new();
  let numbers_called: Vec<&str> = blocks[0].split(",").collect();

  for block in &blocks[1..] {
    let mut board: BingoBoard = BingoBoard { values: [[0; 5]; 5] };
    let nums: Vec<&str> = block.split(" ").collect();
    let mut i = 0;
    let mut j = 0;
    for num in nums {
      if !num.eq("") {
        board.values[i][j] = num.parse::<i32>().unwrap();
        j += 1;
        i += j % 5;
        j = j % 5;
      }
      println!("{} {}", i, j);
    }
    boards.push(board);
  }
}
