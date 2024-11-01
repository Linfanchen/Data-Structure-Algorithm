#include <stdio.h>

/**
 * Selection sort by C Lang.
 *
 *  params:
 *      array -- the data need to sort
 *      n -- the length of array
 */
void selectSort(int arr[], int n)
{
    // Notice: outter loop max running time is `n-2`
    for (size_t i = 0; i < n - 1; i++)
    {
        // Assume the current position holds the minimum element
        int minIndex = i;

        // Find the minimun in arr[i+1...n].
        for (size_t j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                // Update minIndex if a smaller element is found
                minIndex = j;
            }
        }

        // Move minimum element to its correct position
        if (minIndex != i)
        {
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
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
    int arr[] = {40, 20, 30, 60, 10, 50};
    // calculate the length of a array
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("before sort: \n");
    printArray(arr, n);

    selectSort(arr, n - 1);

    printf("after sort: \n");
    printArray(arr, n);

    return 0;
}