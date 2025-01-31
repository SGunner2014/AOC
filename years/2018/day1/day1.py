from typing import List


def parse_file(file_name: str) -> List[int]:
  h = open(file_name, "r")
  lines = [int(x) for x in h.readlines()]
  h.close()
  return lines


def day1_part1(lst: List[int]):
  return sum(lst)


def day1_part2(lst: List[int]):
  current_freq = 0
  freqs = set()
  while True:
    for i in lst:
      current_freq += i
      if current_freq in freqs:
        return current_freq
      else:
        freqs.add(current_freq)


def day1_main():
  tests = {"example.txt": [3, 2]}

  for (filename, results) in tests.items():
    contents = parse_file(filename)
    assert day1_part1(contents) == results[0]
    assert day1_part2(contents) == results[1]

  contents = parse_file("input.txt")
  result = day1_part1(contents)
  print("Part 1: " + str(result))

  result = day1_part2(contents)
  print("Part 2: " + str(result))
