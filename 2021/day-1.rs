use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::VecDeque;

fn _attempt_1() {
  let file = File::open("input/day-1.txt").unwrap();
  let reader = BufReader::new(file);

  let mut window: VecDeque<i32> = VecDeque::new();
  let mut running_sum: i32 = 0;
  let mut last_num: i32 = std::i32::MAX;
  let mut ans_p1: u32 = 0;
  let mut ans_p2: u32 = 0;

  for line in reader.lines() {
    let num: i32 = line.unwrap().parse().unwrap();
    if window.len() >= 3 {
      let old_sum = running_sum;
      running_sum = running_sum - window.pop_front().unwrap() + num;
      if running_sum > old_sum {
        ans_p2 += 1;
      }
    }
    window.push_back(num);
    if num > last_num {
      ans_p1 += 1;
    }
    last_num = num;
  }

  println!("{}", ans_p1);
  println!("{}", ans_p2);
}

fn main() {
  let lines = include_str!("input/day-1.txt").lines();
  let rest = lines.map(|n| n.parse().unwrap()).collect::<Vec<u16>>();
}
