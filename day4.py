from io import TextIOWrapper
from typing import List
import re


def _get_diagonal_indices(side_len: int) -> List[List[int]]:
    diagonal_indices = []
    # gather first half - we're going down the rows
    # 1 1 1 |     ^
    # 1 1 . |   / down and up+right
    # 1 . . v /
    for d in range(side_len):
        indices = []
        # length of the diagonal grows once every iteration
        for x in range(d + 1):
            #                  go down rows     get diagonals
            indices.append(d * side_len - (x * (side_len - 1)))
        diagonal_indices.append(indices)

    # gather second half - going across the last row save the first index that
    # was gathered in the first half
    # . . .       ^
    # . . 2      / across and up+right
    # . 2 2 -->/
    for d in range(side_len - 1, 0, -1):
        indices = []
        # length of the diagonal grows once every iteration
        for y in range(d):
            indices.append(
                # start at last row           move along col   get diagonals
                ((side_len - 1) * side_len)
                + (side_len - d)
                - (y * (side_len - 1))
            )
        diagonal_indices.append(indices)

    return diagonal_indices


def _get_other_diagonal_indices(side_len: int) -> List[List[int]]:
    diagonal_indices = []
    # gather first half - we're going back across the first column
    # 1 1 1 \<----
    # . 1 1   \  back across and down+right
    # . . 1     v
    for d in range(side_len - 1, -1, -1):
        indices = []
        # length of the diagonal grows once every iteration
        for x in range(side_len - d):
            #                going back the first col      get diagonals
            indices.append(side_len - (side_len - d) + (x * (side_len + 1)))
        diagonal_indices.append(indices)

    # gather second half - going down the rows save for the first one
    # . . . | \
    # 2 . . |   \ down and down+right
    # 2 2 . v    v
    for d in range(1, side_len):
        indices = []
        # length of the diagonal grows once every iteration
        for y in range(side_len - d):
            #                 start at second row     get diagonals
            indices.append((d * side_len) + (y * (side_len + 1)))
        diagonal_indices.append(indices)

    return diagonal_indices


def _get_diagonals(block: str, side_len: int) -> List[str]:
    """We're assuming a square block always (row and col are the same)"""
    all_indices = _get_diagonal_indices(side_len)
    lines = []

    for diagonal_indices in all_indices:
        line = ""
        for index in diagonal_indices:
            line = line + block[index]
        lines.append(line)
    return lines


def _get_other_diagonals(block: str, side_len: int) -> List[str]:
    """We're assuming a square block always (row and col are the same)"""
    all_indices = _get_other_diagonal_indices(side_len)
    lines = []

    for diagonal_indices in all_indices:
        line = ""
        for index in diagonal_indices:
            line = line + block[index]
        lines.append(line)
    return lines


def part1(input: TextIOWrapper):
    xmas_count: int = 0

    # Horizontal (forward and backwards)
    pattern = re.compile(r"XMAS")
    rev_pattern = re.compile(r"SAMX")
    for line in input.readlines():
        xmas_count = xmas_count + len(list(pattern.finditer(line)))
        xmas_count = xmas_count + len(list(rev_pattern.finditer(line)))

    # Vertical (forward and backwards)
    input.seek(0)
    # get the whole input as a single string
    no_break_input = input.read().replace("\n", "")
    # transpose the columns into rows and run the same re pattern as above
    for r in range(140):
        line = ""
        for c in range(140):
            line = line + no_break_input[c * 140 + r]
        xmas_count = xmas_count + len(list(pattern.finditer(line)))
        xmas_count = xmas_count + len(list(rev_pattern.finditer(line)))

    # Diagonal (forward and backwards)
    # There are 140 * 2 - 1 left to right diagonals and 140 * 2 - 1 right to
    # left diagonals
    # We turn a square into lines of diagonals by rotating 45 degrees
    #          o      o
    # ooo     o o     oo
    # ooo -> o o o -> ooo
    # ooo     o o     oo
    #          o      o
    # Left to right
    for diagonal in _get_diagonals(no_break_input, 140):
        xmas_count = xmas_count + len(list(pattern.finditer(diagonal)))
        xmas_count = xmas_count + len(list(rev_pattern.finditer(diagonal)))
    # Right to left
    for diagonal in _get_other_diagonals(no_break_input, 140):
        xmas_count = xmas_count + len(list(pattern.finditer(diagonal)))
        xmas_count = xmas_count + len(list(rev_pattern.finditer(diagonal)))

    print(f"{xmas_count=}")


def part2(input: TextIOWrapper):
    mas_count: int = 0

    pattern = re.compile(r"MAS")
    rev_pattern = re.compile(r"SAM")
    no_break_input = input.read().replace("\n", "")

    # The index of the A in the MAS/SAM in the input is going to be the same for
    # left to right and right to left diagonals since its a cross
    # So we calculate all the indices of As in MAS/SAM matches and compare
    # across lists and count how many times they show up in both lists
    ltr_middle_index_matches = set()
    rtl_middle_index_matches = set()

    # Left to right
    ltr_diagonal_indices = _get_diagonal_indices(140)
    for i, diagonal in enumerate(_get_diagonals(no_break_input, 140)):
        for match in pattern.finditer(diagonal):
            # get the index of the A in MAS
            actual_block_index = ltr_diagonal_indices[i][match.start() + 1]
            ltr_middle_index_matches.add(actual_block_index)
        for match in rev_pattern.finditer(diagonal):
            # get the index of the A in SAM
            actual_block_index = ltr_diagonal_indices[i][match.start() + 1]
            ltr_middle_index_matches.add(actual_block_index)

    # Right to left
    rtl_diagonal_indices = _get_other_diagonal_indices(140)
    for i, diagonal in enumerate(_get_other_diagonals(no_break_input, 140)):
        for match in pattern.finditer(diagonal):
            # get the index of the A in MAS
            actual_block_index = rtl_diagonal_indices[i][match.start() + 1]
            rtl_middle_index_matches.add(actual_block_index)
        for match in rev_pattern.finditer(diagonal):
            # get the index of the A in SAM
            actual_block_index = rtl_diagonal_indices[i][match.start() + 1]
            rtl_middle_index_matches.add(actual_block_index)

    mas_count = len(ltr_middle_index_matches & rtl_middle_index_matches)

    print(f"{mas_count=}")
