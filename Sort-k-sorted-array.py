import heapq

def sort_k_sorted_array(arr, k):
    heap = []
    result = []

    # Push first k+1 elements into heap
    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])

    # Process remaining elements
    for i in range(k + 1, len(arr)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    # Extract remaining elements
    while heap:
        result.append(heapq.heappop(heap))

    return result


# Example
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(sort_k_sorted_array(arr, k))
