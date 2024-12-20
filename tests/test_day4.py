from day4 import (
    _get_diagonals,
    _get_other_diagonals,
    _get_diagonal_indices,
    _get_other_diagonal_indices,
)


def test_get_diagonal_indices():
    # fmt: off
    _ = (
        "ABCDEF"
        "GHIJKL"
        "MNOPQR"
        "STUVWX"
        "YZ1234"
        "567890"
    )

    expected = [
        [0],
        [6, 1],
        [12, 7, 2],
        [18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [30, 25, 20, 15, 10, 5],
        [31, 26, 21, 16, 11],
        [32, 27, 22, 17],
        [33, 28, 23],
        [34, 29],
        [35],
    ]

    assert _get_diagonal_indices(6) == expected


def test_get_other_diagonal_indices():
    # fmt: off
    _ = (
        "ABCDEF"
        "GHIJKL"
        "MNOPQR"
        "STUVWX"
        "YZ1234"
        "567890"
    )

    expected = [
        [5],
        [4, 11],
        [3, 10, 17],
        [2, 9, 16, 23],
        [1, 8, 15, 22, 29],
        [0, 7, 14, 21, 28, 35],
        [6, 13, 20, 27, 34],
        [12, 19, 26, 33],
        [18, 25, 32],
        [24, 31],
        [30],
    ]

    assert _get_other_diagonal_indices(6) == expected


def test_get_diagonals():
    # fmt: off
    input = (
        "ABCDEF"
        "GHIJKL"
        "MNOPQR"
        "STUVWX"
        "YZ1234"
        "567890"
    )

    expected = [
        "A",
        "GB",
        "MHC",
        "SNID",
        "YTOJE",
        "5ZUPKF",
        "61VQL",
        "72WR",
        "83X",
        "94",
        "0",
    ]

    assert _get_diagonals(input, 6) == expected


def test_get_other_diagonals():
    # fmt: off
    input = (
        "ABCDEF"
        "GHIJKL"
        "MNOPQR"
        "STUVWX"
        "YZ1234"
        "567890"
    )

    expected = [
        "F",
        "EL",
        "DKR",
        "CJQX",
        "BIPW4",
        "AHOV30",
        "GNU29",
        "MT18",
        "SZ7",
        "Y6",
        "5",
    ]

    assert _get_other_diagonals(input, 6) == expected
