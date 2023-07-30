def insertionSort(arr):
    for step in range(1, len(arr) - 1):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


data = [1, 3, 88, 785, 2, 9, 4, 6, 44, 23, 3, 23, 123]
insertionSort(data)
print("Printing the sorted array: \n")
print(data)