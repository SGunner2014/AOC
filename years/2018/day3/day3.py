import re

from typing import List, Dict, Tuple


def parse_file(filename: str):
  h = open(filename, "r")
  contents = [line.strip() for line in h.readlines()]
  h.close()

  out = []
  for line in contents:
    vals = re.findall(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    vals = list(vals[0])
    vals = tuple([int(i) for i in vals])
    out += [vals]
  return out


# Input: List[(index, x, y, width, height)]
def part1(claims: List[Tuple[int, int, int, int, int]]) -> int:
  def process_claim(claim: Tuple[int, int, int, int, int],
                    map: Dict[str, int]) -> Dict[str, int]:
    (_, x, y, w, h) = claim
    for i in range(x, x + w):
      for j in range(y, y + h):
        map[f"{i}.{j}"] = map.get(f"{i}.{j}", 0) + 1

    return map

  # "x.y" -> int
  map: Dict[str, int] = {}

  for claim in claims:
    map = process_claim(claim, map)

  return sum([1 if v > 1 else 0 for v in map.values()])


def part2(claims: List[Tuple[int, int, int, int, int]]) -> int:
  valid_claims = set([claim[0] for claim in claims])
  
  def process_claim(claim: Tuple[int, int, int, int, int],
                    map: Dict[str, int]) -> Dict[str, int]:
    (id, x, y, w, h) = claim
    for i in range(x, x + w):
      for j in range(y, y + h):
        if f"{i}.{j}" in map:
          if id in valid_claims:
            valid_claims.remove(id)
          if map[f"{i}.{j}"] in valid_claims:
            valid_claims.remove(map[f"{i}.{j}"])
        else:
          map[f"{i}.{j}"] = id

    return map

  # "x.y" -> int
  map: Dict[str, int] = {}

  for claim in claims:
    map = process_claim(claim, map)

  return list(valid_claims)[0]


tests = {"example.txt": [4, 3]}
