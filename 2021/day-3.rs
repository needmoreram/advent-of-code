use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
  let file = File::open("input/day-3.txt").unwrap();
  let reader = BufReader::new(file);

  let num_total_bits = 12;
  let mut counts: Vec<u32> = vec![0; num_total_bits];
  let mut num_entries = 0;

  for line in reader.lines() {
    let line = line.unwrap();
    for (index, ch) in line.chars().enumerate() {
      if ch == '1' {
        counts[index] += 1;
      }
    }
    num_entries += 1;
  }

  let mut gamma_rate = 0;
  let mut epsilon_rate = 0;

  for (index, count) in counts.iter().enumerate() {
    let amt = 1 << (num_total_bits - index - 1);
    if count > &(num_entries / 2) {
      gamma_rate += amt;
    } else {
      epsilon_rate += amt;
    }
  }

  println!("{}", gamma_rate * epsilon_rate);
}
