#include <stdio.h>

/**
 * swap two number
 */
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/**
 * Quick sort by C Lang.
 *
 * params:
 *   arr -- the data array
 *   left -- the first index of arr
 *   right -- the last index of arr
 *
 */
int partition(int arr[], int left, int right) {
    int pivotIndex = left;
    int prev = left;
    int cur = left + 1;

    while (cur <= right) {
        if (arr[cur] < arr[pivotIndex] && ++prev != cur) {
            swap(&arr[prev], &arr[cur]);
        }
        cur++;
    }
    swap(&arr[prev], &arr[pivotIndex]);
    return prev;
}

void quickSort(int arr[], int left, int right) {
    if (left < right) {
        int pivot_index = partition(arr, left, right);
        quickSort(arr, left, pivot_index - 1);
        quickSort(arr, pivot_index + 1, right);
    }
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {30, 40, 60, 10, 20, 50};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Before sorting:\n");
    print_array(arr, n);

    quickSort(arr, 0, n - 1);

    printf("After sorting:\n");
    print_array(arr, n);

    return 0;
}
