#include <stdio.h>

/**
 * swap two number
 */
void swap(int *a, int *b)
{
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
int partition(int arr[], int left, int right)
{
    // init data
    int pivotIndex = left;
    int i = left, j = right;

    while (i < j)
    {
        // right -> left: find the first element less than pivot
        while (i < j && arr[j] > arr[pivotIndex])
        {
            j--;
        }

        // left -> right: find the first element great than pivot
        while (i < j && arr[i] < arr[pivotIndex])
        {
            i++;
        }

        // after upper two loop, indicate that it is able to swap
        if (i < j)
            swap(&arr[i], &arr[j]);
    }

    // Swap the pivot with the element pointed by the right pointer
    swap(&arr[pivotIndex], &arr[j]);

    return j;
}

void quickSort(int arr[], int left, int right)
{
    if (left < right)
    {
        int pivotIndex = partition(arr, left, right);
        quickSort(arr, left, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, right);
    }
}

/**
 * show array
 */
void printArray(int array[], int n)
{
    for (size_t i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n\n");
}

int main()
{
    int arr[] = {40, 20, 30, 60, 10, 50};

    // calculate the length of a array
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("before sort: \n");
    printArray(arr, n);

    // The third param must be `n -1`
    quickSort(arr, 0, n - 1);

    printf("after sort: \n");
    printArray(arr, n);

    return 0;
}