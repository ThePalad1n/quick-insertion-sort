import time
import random

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

def run_test_case(arr):
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

# Test cases:
test_case_1u = random.sample(range(1000), 1000)  # Randomly shuffled array of 1000 unique values
test_case_1s = [i for i in range(1000, 0, -1)]  # Reversed-sorted array of 1000 values
test_case_2u = random.sample(range(10000), 10000)  # Randomly shuffled array of 10000 unique values
test_case_2s = [i for i in range(10000, 0, -1)]  # Reversed-sorted array of 10000 values
test_case_3u = random.sample(range(100000), 100000)  # Randomly shuffled array of 100000 unique values
test_case_3s = [i for i in range(100000, 0, -1)]  # Reversed-sorted array of 100000 values

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