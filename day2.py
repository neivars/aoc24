from io import TextIOWrapper
from itertools import pairwise
from typing import List, Literal, Tuple


def _isolate_bad_level_candidates(
    report: List[int], indices: Tuple[int, int]
) -> Tuple[List[int], List[int]]:
    first_half = report.copy()
    first_half.pop(indices[0])
    second_half = report.copy()
    second_half.pop(indices[1])
    return (first_half, second_half)


def _is_report_safe(report: List[int], tolerance: int = 0) -> bool:
    # Base case of recurison. We're done tolerating bad levels
    if tolerance < 0:
        return False

    # Assume ascending to start
    order: Literal["ASC", "DESC"] = "ASC"

    for i, level_pair in enumerate(pairwise(report)):
        # First pair might update order
        if i == 0:
            if level_pair[0] > level_pair[1]:
                order = "DESC"

        # Test difference
        difference = abs(level_pair[0] - level_pair[1])
        if difference > 3 or difference < 1:

            # EDGE-CASE
            # The recursion will never check if removing the first level makes
            # the report safe. If there's a problem on the second pair (i=1)
            # then explicitly check if removing first level would help
            # e.g 1 4 3 2 1 => removing the first 1 would make report safe
            if i == 1:
                candidates = _isolate_bad_level_candidates(report, (0, 1))
                if _is_report_safe(
                    candidates[0], tolerance=tolerance - 1
                ) or _is_report_safe(candidates[1], tolerance=tolerance - 1):
                    return True
            candidates = _isolate_bad_level_candidates(report, (i, i + 1))
            # Check with either levels in the pair removed, either might be
            # recoverable or none (in which case it returns False from the
            # recursion)
            return _is_report_safe(
                candidates[0], tolerance=tolerance - 1
            ) or _is_report_safe(candidates[1], tolerance=tolerance - 1)

        # Check order
        if (
            order == "ASC"
            and level_pair[0] > level_pair[1]
            or order == "DESC"
            and level_pair[0] < level_pair[1]
        ):
            # EDGE-CASE, see above
            if i == 1:
                candidates = _isolate_bad_level_candidates(report, (0, 1))
                if _is_report_safe(
                    candidates[0], tolerance=tolerance - 1
                ) or _is_report_safe(candidates[1], tolerance=tolerance - 1):
                    return True
            candidates = _isolate_bad_level_candidates(report, (i, i + 1))
            return _is_report_safe(
                candidates[0], tolerance=tolerance - 1
            ) or _is_report_safe(candidates[1], tolerance=tolerance - 1)

    return True


def part1(input: TextIOWrapper):
    safe_reports: int = 0

    for report in input.readlines():
        report = report.strip()
        report = [int(level) for level in report.split(" ")]
        if _is_report_safe(report):
            safe_reports = safe_reports + 1

    print(f"{safe_reports=}")


def part2(input: TextIOWrapper):
    safe_reports: int = 0

    with open("logs/2_2.log", "w") as log:
        for report in input.readlines():
            report = report.strip()
            report = [int(level) for level in report.split(" ")]
            if _is_report_safe(report, tolerance=1):
                safe_reports = safe_reports + 1
            else:
                log.write(str(report) + "\n")

    print(f"{safe_reports=}")
