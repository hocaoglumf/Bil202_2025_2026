def heapify(arr, n, i):
    largest = i          # root
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify reduced heap
        heapify(arr, i, 0)


# Example usage
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print(arr)  # Output: [1, 3, 4, 5, 10]