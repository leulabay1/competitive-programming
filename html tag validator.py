from random import randint
from time import time


def insertion_sort(arr):
    global counterInsertionSort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            counterInsertionSort += 1
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


def merge_sort(arr):
    #base case
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(lt, rt):
    merged = []
    i = 0
    j = 0
    global counterMergeSort

    while i < len(lt) and j < len(rt):
        if lt[i] <= rt[j]:
            counterMergeSort += 1
            merged.append(lt[i])
            i += 1
        else:
            counterMergeSort += 1
            merged.append(rt[j])
            j += 1

    return merged + lt[i:] + rt[j:]

def quickSort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = partition(arr, left, right)

        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)

        return arr,

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    global counterQuickSort

    for j in range(l, r):
        if arr[j] <= pivot:
            counterQuickSort += 1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1


if __name__ == '__main__':

    arr1 = [randint(1, 50) for i in range(10000)]
    arr2 = list(range(10000))
    arr3 = list(range(10000, -1, -1))
    arr4 = [randint(1,50) for i in range(7)]

    counterInsertionSort = 0
    arrInsertion1 = arr1.copy()
    beginInsertionSort = time()
    insertion_sort(arrInsertion1)
    endInsertionSort = time()
    print("Elapsed time of insertion sort with random inputs: {:.10f} and count: {:}".format(endInsertionSort - beginInsertionSort,
                                                                           counterInsertionSort))

    counterInsertionSort = 0
    arrInsertion2 = arr2.copy()
    beginInsertionSort = time()
    insertion_sort(arrInsertion2)
    endInsertionSort = time()
    print("Elapsed time of insertion sort with ascending inputs: {:.10f} and count: {:}".format(endInsertionSort - beginInsertionSort,
                                                                          counterInsertionSort))

    counterInsertionSort = 0
    arrInsertion3 = arr3.copy()
    beginInsertionSort = time()
    insertion_sort(arrInsertion3)
    endInsertionSort = time()
    print("Elapsed time of insertion sort with descending inputs: {:.10f} and count: {:}".format(endInsertionSort - beginInsertionSort,
                                                                          counterInsertionSort))

    counterInsertionSort = 0
    arrInsertion4 = arr4.copy()
    beginInsertionSort = time()
    insertion_sort(arrInsertion4)
    endInsertionSort = time()
    print("Elapsed time of insertion sort with few inputs: {:.10f} and count: {:}".format(endInsertionSort - beginInsertionSort,
                                                                          counterInsertionSort))
    print("\nInsertion sort has Ω(n) and O(n^2)")

    print("-" * 85)
    counterMergeSort = 0
    arrMerge1 = arr1.copy()
    beginMergeSort = time()
    merge_sort(arrMerge1)
    endMergeSort = time()
    print("Elapsed time of merge sort with random inputs: {:.10f} and count: {:}".format(endMergeSort - beginMergeSort,
                                                                         counterMergeSort))

    counterMergeSort = 0
    arrMerge2 = arr2.copy()
    beginMergeSort = time()
    merge_sort(arrMerge2)
    endMergeSort = time()
    print("Elapsed time of merge sort with ascending inputs: {:.10f} and count: {:}".format(endMergeSort - beginMergeSort,
                                                                      counterMergeSort))

    counterMergeSort = 0
    arrMerge3 = arr3.copy()
    beginMergeSort = time()
    merge_sort(arrMerge3)
    endMergeSort = time()
    print("Elapsed time of merge sort with descending inputs: {:.10f} and count: {:}".format(endMergeSort - beginMergeSort,
                                                                      counterMergeSort))

    counterMergeSort = 0
    arrMerge4 = arr4.copy()
    beginMergeSort = time()
    merge_sort(arrMerge4)
    endMergeSort = time()
    print("Elapsed time of merge sort with few inputs: {:.10f} and count: {:}".format(endMergeSort - beginMergeSort,
                                                                      counterMergeSort))
    print("\nMerge sort has Ω(nlogn) and O(nlogn)")
    print("-" * 85)

    counterQuickSort = 0
    arrQuickSort1 = arr1.copy()
    beginQuickSort = time()
    quickSort(arrQuickSort1)
    endQuickSort = time()
    print("Elapsed time of quick sort with random inputs: {:.10f} and count: {:}".format(endQuickSort - beginQuickSort,
                                                                       counterQuickSort))

    counterQuickSort = 0
    arrQuickSort2 = arr2.copy()[:500]
    beginQuickSort = time()
    quickSort(arrQuickSort2)
    endQuickSort = time()
    print("Elapsed time of quick sort with ascending inputs: {:.10f} and count: {:}".format(endQuickSort - beginQuickSort,
                                                                      counterQuickSort))

    counterQuickSort = 0
    arrQuickSort3 = arr3.copy()[:500]
    beginQuickSort = time()
    quickSort(arrQuickSort3)
    endQuickSort = time()
    print("Elapsed time of quick sort with descending inputs: {:.10f} and count: {:}".format(endQuickSort - beginQuickSort,
                                                                      counterQuickSort))

    counterQuickSort = 0
    arrQuickSort4 = arr4.copy()
    beginQuickSort = time()
    quickSort(arrQuickSort4)
    endQuickSort = time()
    print("Elapsed time of quick sort with few inputs: {:.10f} and count: {:}".format(endQuickSort - beginQuickSort,
                                                                      counterQuickSort))

    print("\nQuick sort has Ω(nlogn) and O(n^2)")
