def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = [21, 36, 1, 13, 8, 48, 10]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
