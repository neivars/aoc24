import argparse

import day1
import day2
import day3
import day4
import day5


IMPLEMENTATIONS = {
    (1, 1): day1.part1,
    (1, 2): day1.part2,
    (2, 1): day2.part1,
    (2, 2): day2.part2,
    (3, 1): day3.part1,
    (3, 2): day3.part2,
    (4, 1): day4.part1,
    (4, 2): day4.part2,
    (5, 1): day5.part1,
    (5, 2): day5.part2,
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)
    # use the same input as part 1
    parser.add_argument("-s", action="store_true")

    return parser.parse_args()


def main(day: int, part: int, same_input: bool):
    if part not in [1, 2]:
        raise ValueError("Part can only be 1 or 2.")
    if day < 1 or day > 31:
        raise ValueError("Day can only be between 1 and 31.")

    input_path = f"inputs/{day}_{1 if same_input else part}.txt"
    with open(input_path, "r") as input_f:
        IMPLEMENTATIONS[(day, part)](input_f)


if __name__ == "__main__":
    args = parse_arguments()
    main(args.day, args.part, args.s)
