#include <stdio.h>
#include <stdlib.h>

// 希尔排序函数
void shellSort(int arr[], int n) {
    // 初始步长
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // 对每个步长进行插入排序
        for (int i = gap; i < n; i++) {
            // 保存当前元素
            int temp = arr[i];
            // 对当前元素进行插入排序
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            // 插入当前元素
            arr[j] = temp;
        }
    }
}

int main() {
    int arr[] = {9, 8, 3, 7, 5, 6, 4, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    shellSort(arr, n);

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}