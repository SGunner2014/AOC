from typing import List


# Part 1
def part1(lst: List[str]) -> int:
  letter_twice = 0
  letter_thrice = 0
  for boxID in lst:
    letter_counts = {}
    for char in boxID:
      letter_counts[char] = letter_counts.get(char, 0) + 1
    if 2 in letter_counts.values():
      letter_twice += 1
    if 3 in letter_counts.values():
      letter_thrice += 1
  return letter_twice * letter_thrice


def get_diff(str1, str2) -> List[int]:
  diffs = []

  for x in range(len(str1)):
    if str1[x] != str2[x]:
      diffs.append(x)

  return diffs


# res = get_diff(str1, str2)
# if len(res) == 1:
#   return str1[:res[0]] + str1[res[0] + 1:]

# abc
# abd
# feg
# {a: 2, e: 0, f: 1} a: 2
# {b: 2, e: 1, f: 0} b: 2
# {c: 1, d: 1, g: 1} c: 1


# Part 2
def part2(lst: List[str]) -> str:
  for boxID1 in lst:
    for boxID2 in lst:
      diff = get_diff(boxID1, boxID2)
      if len(diff) == 1:
        return boxID1[:diff[0]] + boxID1[diff[0] + 1:]

  return ""


# Parse
def parse_file(filename):
  h = open(filename, "r")
  contents = [line.strip() for line in h.readlines()]
  h.close()

  return contents


tests = {"example.txt": [12, "fgij"]}
