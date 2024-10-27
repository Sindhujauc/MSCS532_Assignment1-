def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Examplw 1
arr = [12, 11, 13, 5, 6]
insertion_sort_descending(arr)
print("Sorted array in descending order:", arr)


# Example 2
arr = [12, 11, 13, 5, 6, 7, 2000, 80, 11]
insertion_sort_descending(arr)
print("Sorted array in descending order:", arr)
