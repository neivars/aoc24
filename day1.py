from collections import Counter
from io import TextIOWrapper
from typing import List

from printutils import psep


def part1(input: TextIOWrapper):
    lh_list: List[int] = []
    rh_list: List[int] = []

    for line in input.readlines():
        (lh_item, rh_item) = line.split("   ")
        # might have a /n at the end
        rh_item = rh_item.strip()

        lh_item = int(lh_item)
        rh_item = int(rh_item)

        lh_list.append(lh_item)
        rh_list.append(rh_item)

    lh_list = sorted(lh_list)
    rh_list = sorted(rh_list)

    distance: int = 0

    for pair in zip(lh_list, rh_list):
        # absolute distance
        distance = distance + abs(pair[0] - pair[1])

    psep()
    print(f"{distance=}")
    psep()


def part2(input: TextIOWrapper):
    lh_list: List[int] = []
    rh_list: List[int] = []

    for line in input.readlines():
        (lh_item, rh_item) = line.split("   ")
        # might have a /n at the end
        rh_item = rh_item.strip()

        lh_item = int(lh_item)
        rh_item = int(rh_item)

        lh_list.append(lh_item)
        rh_list.append(rh_item)

    counter = Counter(rh_list)
    similarity: int = 0
    for lh_item in lh_list:
        similarity = similarity + (lh_item * counter[lh_item])

    psep()
    print(f"{similarity=}")
    psep()
