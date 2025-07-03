#include <stdio.h>
#include <stdlib.h>

// 交换两个元素
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 调整堆，使以i为根节点的子树满足最大堆的性质
void heapify(int arr[], int n, int i) {
    int largest = i; // 初始化最大值为根节点
    int left = 2 * i + 1; // 左子节点
    int right = 2 * i + 2; // 右子节点

    // 如果左子节点大于根节点
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // 如果右子节点大于当前最大值
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // 如果最大值不是根节点
    if (largest != i) {
        swap(&arr[i], &arr[largest]); // 交换根节点和最大值
        heapify(arr, n, largest); // 递归调整子树
    }
}

// 堆排序函数
void heapSort(int arr[], int n) {
    // 构建最大堆
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // 逐个移除堆顶元素并调整堆
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]); // 交换堆顶元素和最后一个元素
        heapify(arr, i, 0); // 调整剩余的堆
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    heapSort(arr, n);

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}