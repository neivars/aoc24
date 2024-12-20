from graphlib import TopologicalSorter
from io import TextIOWrapper
from typing import List, Set, Dict


def part1(input: TextIOWrapper):
    sum_correct_middle_pages: int = 0
    rules: Dict[int, Set[int]] = {}
    reading_rules = True

    for line in input.readlines():
        if line == "\n":
            # We're done reading the rules
            reading_rules = False
            continue

        line = line.strip()
        if reading_rules:
            dep, node = int(line.split("|")[0]), int(line.split("|")[1])
            if rules.get(node, None) is not None:
                rules[node].add(dep)
            else:
                rules[node] = {dep}
        else:
            pages = [int(p) for p in line.split(",")]
            invalid = False
            for i, page in enumerate(pages):
                deps = rules.get(page, set())
                if len(deps.intersection(pages[i + 1 :])) > 0:
                    invalid = True
            if not invalid:
                sum_correct_middle_pages = (
                    sum_correct_middle_pages + pages[len(pages) // 2]
                )
    print(f"{sum_correct_middle_pages=}")


def part2(input: TextIOWrapper):
    sum_corrected_middle_pages: int = 0
    rules: Dict[int, Set[int]] = {}
    reading_rules = True

    invalid_updates: List[List[int]] = []

    for line in input.readlines():
        if line == "\n":
            # We're done reading the rules
            reading_rules = False
            continue

        line = line.strip()
        if reading_rules:
            dep, node = int(line.split("|")[0]), int(line.split("|")[1])
            if rules.get(node, None) is not None:
                rules[node].add(dep)
            else:
                rules[node] = {dep}
        else:
            pages = [int(p) for p in line.split(",")]
            invalid = False
            for i, page in enumerate(pages):
                deps = rules.get(page, set())
                if len(deps.intersection(pages[i + 1 :])) > 0:
                    invalid = True
                    break
            if invalid:
                invalid_updates.append(pages)

    # We now have all the invalid updates
    for invalid_update in invalid_updates:
        # Build the rules
        ts = TopologicalSorter()
        for page in invalid_update:
            ts.add(page, *rules[page].intersection(invalid_update))
        # ts.prepare()
        correct_order = list(ts.static_order())
        sum_corrected_middle_pages = (
            sum_corrected_middle_pages + correct_order[len(correct_order) // 2]
        )

    print(f"{sum_corrected_middle_pages=}")
