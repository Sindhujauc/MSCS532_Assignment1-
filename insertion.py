def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Examplw 1
arr1 = [12, 11, 13, 5, 6]
insertion_sort_descending(arr1)
print("Sorted array in descending order:", arr1)


# Example 2
arr2 = [12, 11, 13, 5, 6, 7, 2000, 80, 11]
insertion_sort_descending(arr2)
print("Sorted array in descending order:", arr2)


# Example 2
arr3 = [12, 16, 19, 15, 96, 712, 2000, 80, 11]
insertion_sort_descending(arr3)
print("Sorted array in descending order:", arr3)
