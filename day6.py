from enum import IntEnum
from io import TextIOWrapper
from typing import Tuple, Set
from tqdm import tqdm


MAP_SIDE = 130


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def _move(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    """Returns the new position"""
    match direction:
        case Direction.UP:
            # remove a row
            return (pos[0] - 1, pos[1])
        case Direction.DOWN:
            # add a row
            return (pos[0] + 1, pos[1])
        case Direction.RIGHT:
            # add a col
            return (pos[0], pos[1] + 1)
        case Direction.LEFT:
            # remove a col
            return (pos[0], pos[1] - 1)


def _check_oob(pos: int) -> bool:
    """True if out of bounds (oob), False if inside map"""
    if pos[0] < 0 or pos[0] > MAP_SIDE - 1:
        return True
    if pos[1] < 0 or pos[1] > MAP_SIDE - 1:
        return True
    return False


def part1(input: TextIOWrapper):
    patrol_map: Set[Tuple[int, int]] = set()

    positions = set()
    direction = Direction.UP
    guard_position = (0, 0)

    for x, line in enumerate(input.readlines()):
        line = line.strip()
        for y, tile in enumerate(line):
            if tile == "#":
                patrol_map.add((x, y))
            if tile == "^":
                guard_position = (x, y)
                positions.add((x, y))

    t = tqdm(total=MAP_SIDE * MAP_SIDE, ascii=True)
    while True:
        new_pos = _move(guard_position, direction)
        if _check_oob(new_pos):
            break
        if (new_pos[0], new_pos[1]) in patrol_map:
            # Collided, move in clockwise direction
            direction = (direction + 1) % 4
            continue
        positions.add(new_pos)
        guard_position = new_pos

        # make sure we're halting with tqdm progress bar
        t.update()
        t.refresh()
        t.display(f"{guard_position=}")

    print(f"{len(positions)=}")


def part2(input: TextIOWrapper):
    pass
