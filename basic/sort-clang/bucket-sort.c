#include <stdio.h>
#include <stdlib.h>

// 插入排序函数，用于对每个桶内的数据进行排序
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        // 将比key大的元素向后移动
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// 桶排序函数
void bucketSort(int arr[], int n, int bucketCount) {
    // 1. 找到数组中的最大值和最小值
    int max = arr[0];
    int min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }

    // 2. 计算每个桶的范围大小
    int bucketRange = (max - min) / bucketCount + 1;

    // 3. 创建桶数组和记录每个桶大小的数组
    int **buckets = (int **)malloc(bucketCount * sizeof(int *));
    int *bucketSizes = (int *)calloc(bucketCount, sizeof(int));

    // 4. 初始化所有桶
    for (int i = 0; i < bucketCount; i++) {
        buckets[i] = NULL;
        bucketSizes[i] = 0;
    }

    // 5. 将元素分配到各个桶中
    for (int i = 0; i < n; i++) {
        // 计算当前元素应该放入哪个桶
        int bucketIndex = (arr[i] - min) / bucketRange;
        // 处理最大值的情况（确保不会越界）
        if (bucketIndex >= bucketCount) {
            bucketIndex = bucketCount - 1;
        }
        // 动态扩展桶的大小
        buckets[bucketIndex] = (int *)realloc(buckets[bucketIndex],
                                (bucketSizes[bucketIndex] + 1) * sizeof(int));
        // 将元素放入桶中
        buckets[bucketIndex][bucketSizes[bucketIndex]++] = arr[i];
    }

    // 6. 对每个桶内的数据进行排序
    for (int i = 0; i < bucketCount; i++) {
        insertionSort(buckets[i], bucketSizes[i]);
    }

    // 7. 合并所有桶中的数据到原数组
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        for (int j = 0; j < bucketSizes[i]; j++) {
            arr[index++] = buckets[i][j];
        }
        // 释放桶的内存
        free(buckets[i]);
    }

    // 8. 释放桶数组和大小数组的内存
    free(buckets);
    free(bucketSizes);
}

int main() {
    int arr[] = {34, 2, 23, 67, 100, 88};
    int n = sizeof(arr) / sizeof(arr[0]);
    int bucketCount = 3; // 使用3个桶

    printf("原始数组:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bucketSort(arr, n, bucketCount);

    printf("排序后数组:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}