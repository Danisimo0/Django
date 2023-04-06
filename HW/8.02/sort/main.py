import random
import time


# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Сортировка вставками
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# Генерируем массивы разных размеров для сортировки
arr_100 = [random.randint(0, 1000) for i in range(100)]
arr_1000 = [random.randint(0, 1000) for x in range(1000)]

# 100
start = time.time()
bubble_sort(arr_100.copy())
print(f"Bubble sort (100 elements): {time.time() - start:.8f} seconds")

start = time.time()
selection_sort(arr_100.copy())
print(f"Selection sort (100 elements): {time.time() - start:.8f} seconds")

start = time.time()
insertion_sort(arr_100.copy())
print(f"Insertion sort (100 elements): {time.time() - start:.8f} seconds")

start = time.time()
quick_sort(arr_100.copy())
print(f"Quick sort (100 elements): {time.time() - start:.8f} seconds")

start = time.time()
merge_sort(arr_100.copy())
print(f"Merge sort (100 elements): {time.time() - start:.8f} seconds")

# 1000

start = time.time()
bubble_sort(arr_1000.copy())
print(f"Bubble sort (1000 elements): {time.time() - start:.8f} seconds")

start = time.time()
selection_sort(arr_1000.copy())
print(f"Selection sort (1000 elements): {time.time() - start:.8f} seconds")

start = time.time()
insertion_sort(arr_1000.copy())
print(f"Insertion sort (1000 elements): {time.time() - start:.8f} seconds")

start = time.time()
quick_sort(arr_1000.copy())
print(f"Quick sort (1000 elements): {time.time() - start:.8f} seconds")

start = time.time()
merge_sort(arr_1000.copy())
print(f"Merge sort (1000 elements): {time.time() - start:.8f} seconds")

# Bubble sort (100 elements): 0.00193095 seconds
# Selection sort (100 elements): 0.00162053 seconds
# Insertion sort (100 elements): 0.00180697 seconds
# Quick sort (100 elements): 0.00048614 seconds
# Merge sort (100 elements): 0.00074673 seconds
# Bubble sort (1000 elements): 0.35726810 seconds
# Selection sort (1000 elements): 0.23056340 seconds
# Insertion sort (1000 elements): 0.26688194 seconds
# Quick sort (1000 elements): 0.01915455 seconds
# Merge sort (1000 elements): 0.02448702 seconds


# GO Insertion sort
# // 1 run
# // Время работы сортировки вставками для 100 элементов: 12.664µs
# // Время работы сортировки вставками для 1000 элементов: 1.573059ms
#
#
# // 2 run
# // Время работы сортировки вставками для 100 элементов: 12.664µs
# // Время работы сортировки вставками для 1000 элементов: 1.573059ms
#
#
#  // 3 run
# // Время работы сортировки вставками для 100 элементов: 11.327µs
# // Время работы сортировки вставками для 1000 элементов: 986.005µs
