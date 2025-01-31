from typing import List, Tuple

# ..........
# .A........
# ..........
# ........C.
# ...D......
# .....E....
# .B........
# ..........
# ..........
# ........F.


def parse_file(filename: str) -> List[Tuple[int, ...]]:
  h = open(filename, "r")
  lines = h.readlines()
  h.close()

  return [
      tuple([int(part.strip()) for part in line.split(",")]) for line in lines
  ]


def part1(coords: List[Tuple[int, ...]]) -> int:
  #finding maximum extent of the grid
  max_xy = [0, 0]
  max_xy[0] = max(coords, key=lambda coords: coords[0])[0]
  max_xy[1] = max(coords, key=lambda coords: coords[1])[1]

  def getClosestPoint(x, y, coords) -> int:
    """
    Returns ID of closest point, or -1 if > 1
    """
    distances = [abs(x - c_x) + abs(y - c_y) for (c_x, c_y) in coords]

    min_distance = min(distances)
    min_distance_IDs = [
        d for d, i in enumerate(distances) if i == min_distance
    ]

    return -1 if len(min_distance_IDs) > 1 else min_distance_IDs[0]

  def isEdge(x, y):
    return (x == 0 or y == 0 or x == max_xy[0] or y == max_xy[1])

  valid_centres = {}
  for i, _ in enumerate(coords):
    valid_centres[i] = 0

  for x in range(max_xy[0] + 1):
    for y in range(max_xy[1] + 1):
      closestPoint = getClosestPoint(x, y, coords)

      if closestPoint == -1:
        continue

      if isEdge(x, y):
        if closestPoint in valid_centres:
          valid_centres.pop(closestPoint)
      elif closestPoint in valid_centres:
        valid_centres[closestPoint] += 1

  return max(valid_centres.values())


def part2(coords: List[Tuple[int, ...]], *args) -> int:
  max_distance = 10_000
  if len(args) > 0:
    max_distance = args[0]
  
  #finding maximum extent of the grid
  max_xy = [0, 0]
  max_xy[0] = max(coords, key=lambda coords: coords[0])[0]
  max_xy[1] = max(coords, key=lambda coords: coords[1])[1]

  def getTotalDistance(x, y, coords):
    """
    get the sum of all distances to each centre
    """
    distances = [abs(x - c_x) + abs(y - c_y) for (c_x, c_y) in coords]
    return sum(distances)

  region_size = 0  #total size of the region within maximum total distance
  for x in range(max_xy[0] + 1):
    for y in range(max_xy[1] + 1):
      if getTotalDistance(x, y, coords) < max_distance:
        region_size += 1
  
  return region_size


tests = {"example.txt": ([17, 90], 32)}
