def timsort(arr: list[float]) -> list[float]:
    if len(arr) <= 1:
        return arr
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        arr[i:i+min_run] = __insertion_sort(arr[i:i+min_run])
    size = min_run
    while size < n:
        for start in range(0, n, 2*size):
            mid = start + size - 1
            end = min(start + 2*size - 1, n - 1)
            merged = __merge(arr[start:mid+1], arr[mid+1:end+1])
            arr[start:start+len(merged)] = merged
        size *= 2
    return arr


def __merge(left: list[float], right: list[float]) -> list[float]:
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def __insertion_sort(arr: list[float]) -> list[float]:
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = arr[i]
    return arr
