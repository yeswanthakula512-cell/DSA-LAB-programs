def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter element to search: "))

result = linear_search(arr, k)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
