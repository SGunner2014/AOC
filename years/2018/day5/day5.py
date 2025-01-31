def parse_file(filename: str) -> str:
  h = open(filename, "r")
  contents = h.read()
  h.close()

  return contents.strip()


def part1(line: str) -> int:
  def merge_str(line: str) -> str:
    if len(line) <= 1:
      return line
    else:
      a = merge_str(line[:len(line) // 2])
      b = merge_str(line[len(line) // 2:])

      while True:
        if len(a) == 0 or len(b) == 0:
          break
        elif (a[-1] == b[0].lower()
              or a[-1].lower() == b[0]) and a[-1] != b[0]:
          a = a[:-1]
          b = b[1:]
        else:
          break
    return f"{a}{b}"

  processed = merge_str(line)
  return len(processed)


def part2(line: str) -> int:
  def merge_str(line: str, unit: str) -> str:
    if line.lower() == unit.lower():
      return ""
    elif len(line) <= 1:
      return line
    else:
      a = merge_str(line[:len(line) // 2], unit)
      b = merge_str(line[len(line) // 2:], unit)

      while True:
        if len(a) == 0 or len(b) == 0:
          break
        elif (a[-1] == b[0].lower()
              or a[-1].lower() == b[0]) and a[-1] != b[0]:
          a = a[:-1]
          b = b[1:]
        else:
          break
    return f"{a}{b}"

  current_shortest = 99999
  for unitType in "abcdefghijklmnopqrstuvwxyz":
    if unitType in line.lower():
      current_shortest = min(current_shortest, len(merge_str(line, unitType)))

  return current_shortest


tests = {"example.txt": [10, 4]}
