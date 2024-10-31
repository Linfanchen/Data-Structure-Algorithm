#include <stdio.h>

/**
 * Insertion sort by C Lang.
 *
 *  params:
 *      array -- the data need to sort
 *      n -- the length of array
 */
void insertSort(int arr[], int n)
{
    for (size_t i = 0; i < n; i++)
    {
        // Current array element
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j] > key)
        {
            // In the first loop: j + 1 equal to i, indicate that the sorted arr length increased by 1.
            arr[j + 1] = arr[j];
            j--;
        }
        // Put the key in the correct position of an sorted array.
        arr[j + 1] = key;
    }
}

/**
 * show array
 */
void printArray(int arr[], int n)
{
    for (size_t i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
}

int main()
{
    int arr[] = {40, 20, 30, 50, 10};
    // calculate the length of a array
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("before sort: \n");
    printArray(arr, n);

    insertSort(arr, n);

    printf("after sort: \n");
    printArray(arr, n);

    return 0;
}