"""
Day 01 Python Drills: Lists, Slicing, Methods

How to use:
1) Solve each TODO without looking up answers.
2) Run this file and verify outputs with asserts.
3) Refactor once for readability.
"""

from __future__ import annotations


def reverse_with_slicing(values: list[int]) -> list[int]:
    """Return reversed copy using slicing only."""
    # TODO: implement
    return values[::-1]


def every_second(values: list[int]) -> list[int]:
    """Return every second element from index 0."""
    # TODO: implement
    return []


def middle_slice(values: list[int], left: int, right: int) -> list[int]:
    """Return sublist from left (inclusive) to right (exclusive)."""
    # TODO: implement
    return []


def rotate_right(values: list[int], k: int) -> list[int]:
    """Rotate list right by k using slicing."""
    # TODO: implement
    return []


def remove_all_occurrences(values: list[int], target: int) -> list[int]:
    """Return a new list with all target values removed."""
    # TODO: implement (list comprehension recommended)
    return []


def unique_preserve_order(values: list[int]) -> list[int]:
    """Remove duplicates while preserving order."""
    # TODO: implement
    return []


def top_two_sorted_desc(values: list[int]) -> list[int]:
    """Return two largest elements in descending order."""
    # TODO: implement using sort/sorted carefully
    return []


def main() -> None:
    data = [1, 2, 3, 4, 5, 3, 2]

    assert reverse_with_slicing(data) == [2, 3, 5, 4, 3, 2, 1]
    assert every_second(data) == [1, 3, 5, 2]
    assert middle_slice(data, 2, 5) == [3, 4, 5]
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert remove_all_occurrences(data, 2) == [1, 3, 4, 5, 3]
    assert unique_preserve_order(data) == [1, 2, 3, 4, 5]
    assert top_two_sorted_desc([10, 4, 8, 17, 3, 17]) == [17, 17]

    print("Day 01 drills complete. Great work.")


if __name__ == "__main__":
    main()
