# Basic Algorithm

## sort-Clang

### bubble sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/bubble-sort.c )

### bucket sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/bucket-sort.c )

输入数组：
`[34, 2, 23, 67, 100, 88]`

1. 确定最大值和最小值
    - 最大值(max) = 100
    - 最小值(min) = 2

2. 计算桶的范围
   - 桶数量(bucketCount) = 3
   - 桶范围(bucketRange) = (100-2)/3 +1 = 33

3. 创建桶
   - 创建3个空桶：桶0、桶1、桶2

4. 分配元素到桶中。计算每个元素所属的桶索引：(value - min) / bucketRange
    - 34: (34-2)/33 = 0 → 桶0
    - 2: (2-2)/33 = 0 → 桶0
    - 23: (23-2)/33 = 0 → 桶0
    - 67: (67-2)/33 = 1 → 桶1
    - 100: (100-2)/33 = 2 → 桶2
    - 88: (88-2)/33 = 2 → 桶2

    分配结果：
      - 桶0: [34, 2, 23]
     - 桶1: [67]
     - 桶2: [100, 88]

5. 对每个桶进行排序
   - 桶0排序后: [2, 23, 34]
   - 桶1排序后: [67]
   - 桶2排序后: [88, 100]

6. 合并桶，按桶顺序合并：
桶0 + 桶1 + 桶2 = [2, 23, 34, 67, 88, 100]


### heap sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/heap-sort.c )

int arr[] = {12, 11, 13, 5, 6, 7};

1. 构建最大堆：
    - 初始数组：[12, 11, 13, 5, 6, 7]
    - 从最后一个非叶子节点开始调整堆，最后一个非叶子节点的索引为 n / 2 - 1 = 2。
    - 调整索引为2的节点（值为13），不需要调整。
    - 调整索引为1的节点（值为11），不需要调整。
    - 调整索引为0的节点（值为12），交换12和13，得到 [13, 11, 12, 5, 6, 7]。

2. 移除堆顶元素并调整堆：
   - 交换堆顶元素（13）和最后一个元素（7），得到 [7, 11, 12, 5, 6, 13]。
   - 调整剩余的堆 [7, 11, 12, 5, 6]，交换7和12，得到 [12, 11, 7, 5, 6]。
   - 交换堆顶元素（12）和最后一个元素（6），得到 [6, 11, 7, 5, 12, 13]。
   - 调整剩余的堆 [6, 11, 7, 5]，交换6和11，得到 [11, 6, 7, 5]。
   - 交换堆顶元素（11）和最后一个元素（5），得到 [5, 6, 7, 11, 12, 13]。
   - 调整剩余的堆 [5, 6, 7]，不需要调整。
   - 交换堆顶元素（7）和最后一个元素（7），得到 [5, 6, 7, 11, 12, 13]。
   - 调整剩余的堆 [5, 6]，不需要调整。
   - 交换堆顶元素（6）和最后一个元素（6），得到 [5, 6, 7, 11, 12, 13]。
   - 调整剩余的堆 [5]，不需要调整。
   - 交换堆顶元素（5）和最后一个元素（5），得到 [5, 6, 7, 11, 12, 13]。

3. 最终排序结果：
   - 排序后的数组：[5, 6, 7, 11, 12, 13]

### insert sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/insert-sort.c )

### merge sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/merge-sort.c )

int arr[] = {12, 11, 13, 5, 6, 7};

1. 初始数组：
    - [12, 11, 13, 5, 6, 7]

2. 递归分解：
   - 将数组分成两半：[12, 11, 13] 和 [5, 6, 7]。
   - 继续分解 [12, 11, 13]：
   - 分成 [12] 和 [11, 13]。
   - 继续分解 [11, 13]：
   - 分成 [11] 和 [13]。
   - 继续分解 [5, 6, 7]：
   - 分成 [5] 和 [6, 7]。
   - 继续分解 [6, 7]：
   - 分成 [6] 和 [7]。

3. 递归合并：
   - 合并 [11] 和 [13]，得到 [11, 13]。
   - 合并 [12] 和 [11, 13]，得到 [11, 12, 13]。
   - 合并 [6] 和 [7]，得到 [6, 7]。
   - 合并 [5] 和 [6, 7]，得到 [5, 6, 7]。
   - 合并 [11, 12, 13] 和 [5, 6, 7]，得到 [5, 6, 7, 11, 12, 13]。

4. 最终排序结果
   - 排序后的数组：[5, 6, 7, 11, 12, 13]

### quick sort hoare
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/quick-sort-hoare.c )

### quick sort prev cur pointer
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/quick-sort-prev-cur-pointer.c )

### quick sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/quick-sort.c )

### radix sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/radix-sort.c )

int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};

1. 获取最大值：
   - 最大值 max = 802

2. 确定最大位数：
   - 最大值有3位，因此需要对个位、十位和百位分别进行排序。

3. 按个位排序：
   - 初始数组：[170, 45, 75, 90, 802, 24, 2, 66]
   - 按个位排序后：[170, 90, 802, 2, 24, 45, 66, 75]

4. 按十位排序：
   - 按十位排序后：[802, 2, 24, 45, 66, 170, 75, 90]

5. 按百位排序：
   - 按百位排序后：[2, 24, 45, 66, 75, 90, 170, 802]

6. 最终排序结果
   - 排序后的数组：[2, 24, 45, 66, 75, 90, 170, 802]

### select sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/select-sort.c )

### shell-sort
[source code clang](https://github.com/Linfanchen/Data-Structure-Algorithm/blob/main/basic/sort-clang/shell-sort.c )

int arr[] = {9, 8, 3, 7, 5, 6, 4, 1};

初始数组：[9, 8, 3, 7, 5, 6, 4, 1]
1. 第一次分组（步长为4）：
   - 分组：[9, 3] 和 [8, 7] 和 [5, 4] 和 [6, 1]
   - 排序后：[3, 7, 4, 1, 5, 6, 8, 9]
2. 第二次分组（步长为2）：
   - 分组：[3, 4] 和 [7, 1] 和 [5, 8] 和 [6, 9]
   - 排序后：[3, 1, 4, 6, 5, 8, 7, 9]
3. 第三次分组（步长为1）：
   - 分组：[3, 1, 4, 6, 5, 8, 7, 9]
   - 排序后：[1, 3, 4, 5, 6, 7, 8, 9]
4. 最终排序结果
   - 排序后的数组：[1, 3, 4, 5, 6, 7, 8, 9]

## string