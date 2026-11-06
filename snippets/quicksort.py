"""A compact, readable quicksort snippet.

``quicksort`` returns a new list sorted in ascending order. It takes the
middle element as the pivot and splits the input into three groups (smaller,
equal, larger), which keeps the code short and handles duplicate values
naturally.

This is the copy-paste / teaching variant; the in-place Hoare implementation
lives in ``../quicksort/quicksort.py``.
"""

from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def quicksort(items: List[T]) -> List[T]:
    """Return a new list with ``items`` sorted in ascending order."""
    if len(items) <= 1:
        return list(items)

    pivot = items[len(items) // 2]
    smaller = [item for item in items if item < pivot]
    equal = [item for item in items if item == pivot]
    larger = [item for item in items if item > pivot]
    return quicksort(smaller) + equal + quicksort(larger)


def main() -> None:
    print(quicksort([9, 4, 7, 1, 0, 8, 4, 2, 6, 3, 5]))

    samples = [
        [],
        [1],
        [2, 1],
        [5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, -1, 0, -1, 3, 7, 100, -50, 7, 7],
        ["pear", "apple", "fig", "banana", "apple"],
    ]
    for sample in samples:
        assert quicksort(sample) == sorted(sample), sample

    import random

    random.seed(42)
    big = [random.randint(-1_000, 1_000) for _ in range(10_000)]
    assert quicksort(big) == sorted(big)
    print("all checks passed")


if __name__ == "__main__":
    main()
