def binary_search(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = list(map(int, input("Enter sorted elements: ").split()))
k = int(input("Enter element to search: "))

result = binary_search(arr, k)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
