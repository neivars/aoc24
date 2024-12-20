from typing import List, Tuple

import pytest

from day2 import _is_report_safe, _isolate_bad_level_candidates


@pytest.mark.parametrize(
    "report,indices,expected",
    [
        ([1, 2, 3, 4, 5], [0, 1], ([2, 3, 4, 5], [1, 3, 4, 5])),
        ([1, 2, 3, 4, 5], [2, 3], ([1, 2, 4, 5], [1, 2, 3, 5])),
        ([1, 2, 3, 4, 5], [3, 2], ([1, 2, 3, 5], [1, 2, 4, 5])),
        ([1, 2, 3, 4, 5], [1, 4], ([1, 3, 4, 5], [1, 2, 3, 4])),
    ],
)
def test_isolate_bad_level_candidates(
    report: List[int], indices: Tuple[int, int], expected: Tuple[List[int], List[int]]
):
    assert _isolate_bad_level_candidates(report, indices) == expected


@pytest.mark.parametrize(
    "report",
    [
        # ASC
        [1, 2],  # just pair
        [1, 2, 3, 4, 5],  # increase by 1
        [1, 3, 5, 7, 9],  # increase by 2
        [1, 4, 7, 10, 13],  # increase by 3
        [1, 3, 5, 6, 9, 12, 13],  # mixed increase
        # DESC
        [2, 1],
        [5, 4, 3, 2, 1],
        [9, 7, 5, 3, 1],
        [13, 10, 7, 4, 1],
        [13, 12, 9, 6, 5, 3, 1],
    ],
)
def test_safe_reports(report: List[int]):
    assert _is_report_safe(report)


@pytest.mark.parametrize(
    "report",
    [
        # ASC
        [1, 2],  # just pair
        [1, 2, 3, 4, 5],  # increase by 1
        [1, 3, 5, 7, 9],  # increase by 2
        [1, 4, 7, 10, 13],  # increase by 3
        [1, 3, 5, 6, 9, 12, 13],  # mixed increase
        # DESC
        [2, 1],
        [5, 4, 3, 2, 1],
        [9, 7, 5, 3, 1],
        [13, 10, 7, 4, 1],
        [13, 12, 9, 6, 5, 3, 1],
    ],
)
def test_safe_reports_with_tolerance_1(report: List[int]):
    assert _is_report_safe(report, tolerance=1)


@pytest.mark.parametrize(
    "report",
    [
        # ASC
        [1, 2, 2, 4, 5],  # not at least one diff
        [1, 3, 5, 7, 11],  # more than 3
        [1, 4, 7, 6, 9],  # change in order
        [1, 3, 7, 6, 9, 12, 13],  # more than 3 + change in order
        # DESC
        [5, 4, 2, 2, 1],
        [11, 7, 5, 3, 1],
        [9, 6, 7, 4, 1],
        [13, 12, 9, 6, 7, 3, 1],
    ],
)
def test_unsafe_reports(report: List[int]):
    is_safe = _is_report_safe(report)
    assert is_safe is not None
    assert not is_safe


@pytest.mark.parametrize(
    "report",
    [
        # ASC
        [1, 2, 2, 4, 5],  # not at least one diff
        [1, 3, 5, 7, 11],  # more than 3
        [1, 4, 7, 6, 9],  # change in order
        # DESC
        [5, 4, 2, 2, 1],
        [11, 7, 5, 3, 1],
        [9, 6, 7, 4, 1],
        # ASC wrong but works if DESC
        [1, 4, 3, 2, 1],  # removing first 1 makes it safe
        # Input examples
        [9, 12, 14, 16, 17, 18, 15],
        [86, 88, 91, 94, 95, 95],
        [15, 18, 20, 21, 23, 25, 28, 32],
        [70, 72, 74, 77, 78, 83],
    ],
)
def test_unsafe_reports_with_tolerance_1(report: List[int]):
    assert _is_report_safe(report, tolerance=1)


@pytest.mark.parametrize(
    "report",
    [
        # ASC
        [1, 2, 2, 4, 5],  # not at least one diff
        [1, 3, 5, 7, 11],  # more than 3
        [1, 4, 7, 6, 9],  # change in order
        # DESC
        [5, 4, 2, 2, 1],
        [11, 7, 5, 3, 1],
        [9, 6, 7, 4, 1],
        # Input examples
        [90, 91, 92, 92, 95, 95],
        [57, 60, 62, 64, 63, 64, 65],
        [
            44,
            45,
            44,
            47,
            46,
        ],
    ],
)
def test_unsafe_reports_with_tolerance_2(report: List[int]):
    assert _is_report_safe(report, tolerance=2)
