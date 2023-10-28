import time
import random
import sys

sys.setrecursionlimit(10**8)

def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose a random pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap the pivot element with the last element
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    while low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        low = pivot + 1

def run_test_case(arr):
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

# Test cases:
test_case_1u = random.sample(range(1000), 1000)  # Randomly shuffled array of 1000 unique values
test_case_1s = [i for i in range(1000, 0, -1)]  # Reversed-sorted array of 1000 values
test_case_2u = random.sample(range(10000), 10000)  # Randomly shuffled array of 10000 unique values
test_case_2s = [i for i in range(10000, 0, -1)]  # Reversed-sorted array of 10000 values
test_case_3u = random.sample(range(100000), 100000)  # Randomly shuffled array of 10000 unique values
test_case_3s = [i for i in range(100000, 0, -1)]  # Reversed-sorted array of 10000 values

print("Test Case 1 Unique:")
run_test_case(test_case_1u)
print("Test Case 1 Reverse Sorted:")
run_test_case(test_case_1s)
print("Test Case 2 Unique:")
run_test_case(test_case_2u)
print("Test Case 2 Reverse Sorted:")
run_test_case(test_case_2s)
print("Test Case 3 Unique:")
run_test_case(test_case_3u)
print("Test Case 3 Reverse Sorted:")
run_test_case(test_case_3s)