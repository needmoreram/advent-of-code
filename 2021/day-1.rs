fn part1(depths: &[u16]) -> usize {
  return depths.windows(2).filter(|v| v[0] < v[1]).count();
}

fn part2(depths: &[u16]) -> usize {
  return depths.windows(4).filter(|v| v[0] < v[3]).count();
}

fn main() {
  let lines = include_str!("input/day-1.txt").lines();
  let depths = lines.map(|n| n.parse().unwrap()).collect::<Vec<u16>>();
  println!("{}", part1(&depths));
  println!("{}", part2(&depths));
}
