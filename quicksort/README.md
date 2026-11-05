# 快速排序（Java / Python）

同一套算法的两个实现：原地排序、Hoare 式双指针分区、取中间元素为 pivot。
每次分区后只对较小的一半递归，较大的一半用循环处理，因此递归深度为 O(log n)，
对已有序、逆序和大量重复元素的输入也不会退化到 O(n²) 的递归深度。

| 文件 | 说明 |
| --- | --- |
| `Quicksort.java` | `Quicksort.sort(int[])`，原地排序，附带 `main` 自检 |
| `quicksort.py` | `quicksort(items)`，原地排序并返回该列表，附带 `main` 自检 |

## 运行

```bash
# Java（JDK 8+）
cd quicksort
javac Quicksort.java
java -cp . Quicksort

# Python（3.9+）
cd quicksort
python quicksort.py
```

两个 `main` 都会运行空数组、单元素、全部重复、已排序、逆序、随机大数组等自检，
输出 `all checks passed` 即表示通过。

## 复杂度

- 平均 / 最好：O(n log n)
- 最坏（极端不平衡分区）：O(n²)，中间 pivot 与“只递归较小一侧”显著降低触发概率
- 额外空间：O(log n) 递归栈，排序本身原地进行
