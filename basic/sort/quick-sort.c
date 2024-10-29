#include <stdio.h>

/**
 * Quick sort by C Lang.
 *
 * params:
 *   arr -- the data array
 *   left -- the first index of arr
 *   right -- the last index of arr
 *
 */
void quickSort(int arr[], int left, int right)
{
    // the arr is empty or left one element
    if (left >= right)
    {
        return;
    }

    // init data
    int pivot = arr[left];
    int i = left, j = right;

    while (i < j)
    {
        // right -> left: find the first element less than pivot
        // notice: when arr[j] meet the condition `arr[j] < pivot`, it will break the while loop, indicate that current element is less than pivot.
        while (i < j && arr[j] > pivot)
            j--;
        if (i < j)
        {
            arr[i++] = arr[j];
        }

        // left -> right: find the first element great than pivot
        while (i < j && arr[i] < pivot)
            i++;
        if (i < j)
        {
            arr[j--] = arr[i];
        }

        arr[i] = pivot; // The element has benn correctly placed in its corresponding position

        quickSort(arr, left, i - 1);  // Recursive invoke in the left sub array
        quickSort(arr, i + 1, right); // Recursive invoke in the right sub array
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

    quickSort(arr, 0, n);

    printf("after sort: \n");
    printArray(arr, n);

    return 0;
}