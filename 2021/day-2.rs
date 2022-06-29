fn main() {
  let lines = include_str!("input/day-2.txt").lines();
  let instructions = lines.map(|v| v.split_once(' ').unwrap());
  let (depth1, hpos, depth2, _) = instructions.fold(
    (0, 0, 0, 0), |(d1, h, d2, a), (i, v)| {
      match (i, v.parse::<i32>().unwrap()) {
        ("forward", v) => (  d1  , h + v, d2 + a * v,   a  ),
        (   "down", v) => (d1 + v,   h  ,      d2   , a + v),
        (     "up", v) => (d1 - v,   h  ,      d2   , a - v),
                     _ => unreachable!()
      }
    }
  );
  println!("{}\n{}", depth1 * hpos, depth2 * hpos);
}
