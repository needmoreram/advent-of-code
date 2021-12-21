package main

import (
  "bufio"
  "fmt"
  "os"
  "strconv"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}

func main() {
  file, err := os.Open("input/day-1.txt")
  check(err)
  defer file.Close()

  var queue []int
  var running_sum int = 0
  var ans_p1 int = 0
  var ans_p2 int = 0

  scanner := bufio.NewScanner(file)
  if scanner.Scan() {
    var num, err = strconv.Atoi(scanner.Text())
    check(err)
    queue = append(queue, num)
    running_sum = running_sum + num
  }
  for scanner.Scan() {
    var old_sum = running_sum
    var num, err = strconv.Atoi(scanner.Text())
    check(err)
    running_sum = running_sum + num
    if num > queue[len(queue)-1] {
      ans_p1 = ans_p1 + 1
    }
    if len(queue) >= 3 {
      running_sum = running_sum - queue[0]
      if running_sum > old_sum {
        ans_p2 = ans_p2 + 1
      }
      queue = queue[1:]
    }
    queue = append(queue, num)
  }

  fmt.Println(ans_p1)
  fmt.Println(ans_p2)
}
