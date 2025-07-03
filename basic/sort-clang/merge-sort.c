#include <stdio.h>
#include <stdlib.h>

// 合并两个有序数组
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1; // 左子数组的大小
    int n2 = right - mid;    // 右子数组的大小

    // 创建临时数组
    int L[n1], R[n2];

    // 拷贝数据到临时数组
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }

    // 合并临时数组
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // 复制剩余的元素
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// 主要的归并排序函数
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2; // 找到中间位置

        // 分别对左右两半进行排序
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // 合并两个有序数组
        merge(arr, left, mid, right);
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

    mergeSort(arr, 0, n - 1);

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}