from typing import Set, Tuple, Dict, List

def parse_file(filename: str) -> Tuple[Set[Tuple[int, int]], Tuple[int, int], int, int]:
    h = open(filename, "r")
    lines = [line.strip() for line in h.readlines()]
    h.close()

    obstructions = set()
    starting_pos = None
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]
            if char == "^":
                starting_pos = (j, i)
            elif char == "#":
                obstructions.add((j, i))

    return obstructions, starting_pos, max_x, max_y


def part1(parsed: Tuple[Set[Tuple[int, int]], Tuple[int, int], int, int]):
    (obstructions, starting_pos, max_x, max_y) = parsed

    visited = set()
    (x, y) = starting_pos

    directions = [
        [1, 0], # right
        [0, 1], # down
        [-1, 0], # left
        [0, -1], # up
    ]

    current_dir = 3

    while max_x >= x > 0 and max_y >= y > 0:
        visited.add((x, y))

        new_x = x + directions[current_dir][0]
        new_y = y + directions[current_dir][1]
        new_direction = current_dir

        while (new_x, new_y) in obstructions:
            new_direction += 1
            if new_direction > 3:
                new_direction = 0

            new_x = x + directions[new_direction][0]
            new_y = y + directions[new_direction][1]

        current_dir = new_direction
        x = new_x
        y = new_y

    return len(visited)


def part2(parsed: Tuple[Set[Tuple[int, int]], Tuple[int, int], int, int]) -> int:
    (obstructions, starting_pos, max_x, max_y) = parsed

    visited: Dict[Tuple[int, int], Set[int]] = {}
    (x, y) = starting_pos

    directions = [
        [1, 0],  # right
        [0, 1],  # down
        [-1, 0],  # left
        [0, -1],  # up
    ]

    current_dir = 3

    while max_x >= x > 0 and max_y >= y > 0:
        if not (x, y) in visited:
            visited[(x, y)] = {current_dir}
        else:
            visited[(x, y)].add(current_dir)

        new_x = x + directions[current_dir][0]
        new_y = y + directions[current_dir][1]
        new_direction = current_dir

        while (new_x, new_y) in obstructions:
            new_direction += 1
            if new_direction > 3:
                new_direction = 0

            new_x = x + directions[new_direction][0]
            new_y = y + directions[new_direction][1]

        current_dir = new_direction
        x = new_x
        y = new_y

    print(str(visited))

    return len(list(filter(lambda visited_dirs: len(visited_dirs) >= 2, visited.values())))


tests = {
    "example.txt": [41, 6]
}