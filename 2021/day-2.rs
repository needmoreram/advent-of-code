use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
  let file = File::open("input/day-2.txt").unwrap();
  let reader = BufReader::new(file);

  let mut hpos = 0;
  let mut depth = 0;
  let mut aim = 0;

  for line in reader.lines() {
    let line = line.unwrap();
    let instr: Vec<&str> = line.split(" ").collect();
    let amount: i32 = instr[1].parse().unwrap();
    if instr[0].eq("forward") {
      hpos += amount;
      depth += aim * amount;
    } else if instr[0].eq("down") {
      aim += amount;
    } else if instr[0].eq("up") {
      aim -= amount;
    } else {
      panic!("Don't know how to '{}'", instr[0]);
    }
  }

  println!("{}", hpos * aim);
  println!("{}", hpos * depth);
}
