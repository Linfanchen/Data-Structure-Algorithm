#include <stdio.h>
#include <stdlib.h>

// 获取最大值
int getMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// 根据指定的位数进行计数排序
void countingSortByDigit(int arr[], int n, int exp) {
    int output[n]; // 输出数组
    int count[10] = {0}; // 计数数组

    // 根据当前位数统计每个数字出现的次数
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }

    // 累加计数数组，得到每个数字在输出数组中的位置
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // 构建输出数组
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    // 将输出数组复制回原数组
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// 主要的基数排序函数
void radixSort(int arr[], int n) {
    // 获取最大值，以确定最大位数
    int max = getMax(arr, n);

    // 从最低位到最高位依次进行计数排序
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSortByDigit(arr, n, exp);
    }
}

int main() {
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    radixSort(arr, n);

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}