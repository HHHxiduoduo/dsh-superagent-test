"""In-place quicksort for lists of comparable items.

Partitioning uses the Hoare-style two-pointer scheme with the middle element
as pivot. After each partition the smaller half is sorted recursively while
the larger half is handled by a loop, so the recursion depth stays O(log n)
even for already-sorted, reverse-sorted or otherwise adversarial inputs.
Duplicate values are handled in linear time per partition and do not degrade
performance to O(n^2).
"""

from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def quicksort(items: List[T]) -> List[T]:
    """Sorts ``items`` in place in ascending order and returns it."""
    _sort_range(items, 0, len(items) - 1)
    return items


def _sort_range(items: List[T], lo: int, hi: int) -> None:
    while lo < hi:
        pivot = items[(lo + hi) // 2]
        left, right = lo, hi

        while left <= right:
            while items[left] < pivot:
                left += 1
            while items[right] > pivot:
                right -= 1
            if left <= right:
                items[left], items[right] = items[right], items[left]
                left += 1
                right -= 1

        # Recurse into the smaller partition and iterate over the larger one
        # to keep the call stack bounded by O(log n).
        if right - lo < hi - left:
            _sort_range(items, lo, right)
            lo = left
        else:
            _sort_range(items, left, hi)
            hi = right


def _check(values: List[T], label: str) -> None:
    expected = sorted(values)
    quicksort(values)
    if values != expected:
        raise AssertionError(f"{label}: expected {expected} but got {values}")


def main() -> None:
    sample = [9, 4, 7, 1, 0, 8, 4, 2, 6, 3, 5]
    quicksort(sample)
    print("sorted sample:", sample)

    _check([], "empty")
    _check([1], "single")
    _check([2, 1], "two elements")
    _check([5, 5, 5, 5], "all duplicates")
    _check([1, 2, 3, 4, 5], "already sorted")
    _check([5, 4, 3, 2, 1], "reverse sorted")
    _check([3, -1, 0, -1, 3, 7, 100, -50, 7, 7], "mixed values")

    import random

    random.seed(42)
    big = [random.randint(-1_000, 1_000) for _ in range(10_000)]
    _check(big, "random 10k values")

    words = ["pear", "apple", "fig", "banana", "apple"]
    quicksort(words)
    assert words == sorted(words), words
    print("sorted words:", words)

    print("all checks passed")


if __name__ == "__main__":
    main()
