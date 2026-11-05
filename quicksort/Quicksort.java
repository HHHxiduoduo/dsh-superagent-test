import java.util.Arrays;
import java.util.Random;

/**
 * In-place quicksort for {@code int} arrays.
 *
 * <p>Partitioning uses the Hoare-style two-pointer scheme with the middle
 * element as pivot. After each partition the smaller half is sorted
 * recursively while the larger half is handled by a loop, so the recursion
 * depth stays O(log n) even for already-sorted, reverse-sorted or otherwise
 * adversarial inputs. Duplicate values are handled in linear time per
 * partition and do not degrade performance to O(n^2).</p>
 */
public final class Quicksort {

    private Quicksort() {
        // Utility class.
    }

    /**
     * Sorts {@code values} in place in ascending order.
     *
     * @param values the array to sort; {@code null} and arrays with fewer
     *               than two elements are left untouched
     */
    public static void sort(int[] values) {
        if (values == null || values.length < 2) {
            return;
        }
        sortRange(values, 0, values.length - 1);
    }

    private static void sortRange(int[] a, int lo, int hi) {
        while (lo < hi) {
            int pivot = a[lo + (hi - lo) / 2];
            int left = lo;
            int right = hi;

            while (left <= right) {
                while (a[left] < pivot) {
                    left++;
                }
                while (a[right] > pivot) {
                    right--;
                }
                if (left <= right) {
                    swap(a, left, right);
                    left++;
                    right--;
                }
            }

            // Recurse into the smaller partition and iterate over the larger
            // one to keep the call stack bounded by O(log n).
            if (right - lo < hi - left) {
                sortRange(a, lo, right);
                lo = left;
            } else {
                sortRange(a, left, hi);
                hi = right;
            }
        }
    }

    private static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    public static void main(String[] args) {
        int[] sample = {9, 4, 7, 1, 0, 8, 4, 2, 6, 3, 5};
        sort(sample);
        System.out.println("sorted sample: " + Arrays.toString(sample));

        check(new int[] {}, "empty");
        check(new int[] {1}, "single");
        check(new int[] {2, 1}, "two elements");
        check(new int[] {5, 5, 5, 5}, "all duplicates");
        check(new int[] {1, 2, 3, 4, 5}, "already sorted");
        check(new int[] {5, 4, 3, 2, 1}, "reverse sorted");
        check(new int[] {3, -1, 0, -1, 3, 7, 100, -50, 7, 7}, "mixed values");

        Random random = new Random(42);
        int[] big = new int[10_000];
        for (int i = 0; i < big.length; i++) {
            big[i] = random.nextInt(2_000) - 1_000;
        }
        check(big, "random 10k values");

        System.out.println("all checks passed");
    }

    private static void check(int[] values, String label) {
        int[] expected = values.clone();
        Arrays.sort(expected);
        sort(values);
        if (!Arrays.equals(values, expected)) {
            throw new AssertionError(label + ": expected " + Arrays.toString(expected)
                    + " but got " + Arrays.toString(values));
        }
    }
}
