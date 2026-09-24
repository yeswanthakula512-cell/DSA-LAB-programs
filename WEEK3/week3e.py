def quicksort(a, low, high):
    if low < high:

        pivot = a[low]

        i = low
        j = high

        while i < j:

            while i <= high and a[i] <= pivot:
                i = i + 1

            while j >= low and a[j] > pivot:
                j = j - 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        a[low], a[j] = a[j], a[low]

        quicksort(a, low, j - 1)
        quicksort(a, j + 1, high)


a = list(map(int, input("Enter elements separated by spaces: ").split()))

n = len(a)

quicksort(a, 0, n - 1)

print("Sorted array:", a)
