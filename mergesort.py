def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    ans = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    ans += left[i:]
    ans += right[j:]

    return ans


arr = list(map(int, input("Enter numbers: ").split()))

print("Input array:", arr)

arr = merge_sort(arr)

print("Sorted array:", arr)