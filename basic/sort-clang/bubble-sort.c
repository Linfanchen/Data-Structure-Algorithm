#include <stdio.h>

/**
 * bubble sort algorithm
 *
 * params:
 *      array -- the data need to sort
 *      n -- the length of array
 */
void bubbleSort(int array[], int n)
{
    int i, j;
    // indicate whether is still swapping in this loop
    int flag;

    for (i = n - 1; i > 0; i--)
    {
        flag = 0; // init in current loop

        for (j = 0; j < i; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;

                flag = 1; // swapped
            }
        }

        if (flag == 0)
        {
            break; // if there is no swapping, it indicates that the array is sorted
        }
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

    bubbleSort(arr, n);

    printf("after sort: \n");
    printArray(arr, n);

    return 0;
}