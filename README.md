# Exploring Hybrid and Adaptive Sorting Algorithms

Author: Evan Green

Date: 10/27/2023

## Table of Contents

- [Objectives](#objectives)
- [Project Components](#project-components)
- [Expected Skills Gained](#expected-skills-gained)
- [Deliverables](#deliverables)
- [Conclusion](#conclusion)

---

### Overview

I started this project with a simple goal in mind: to create a sorting algorithm that could get the job done a bit faster. So, I thought, why not take the best parts of two existing sorting techniques, but which ones should I choose? After deliberating with some peers I decided on Quick Sort and Insertion Sort.

---

### Project Components

#### Algorithm Design

1. **Importing Necessary Modules**
   - `import time`: Imports the time module to allow for timing the execution of the algorithm.
   - `import random`: Imports the random module for generating a random sample of numbers in one of the test cases.
   - `import sys`: This was the most important one in debugging the partitions in quicksort and the hybrid algorithm

2. **Function Definitions**
   a. `insertion_sort(arr, low, high)`: Implements the Insertion Sort algorithm for a specified segment of the array `arr` from index `low` to `high`.
   b. `partition(arr, low, high)`: Implements the partitioning step of the Quick Sort algorithm.
   c. `quick_insertion_sort(arr, low, high, threshold)`: The main function implementing the hybrid Quick-Insertion Sort algorithm.
   d. `run_test_case(arr, threshold)`: Executes a test case, timing the execution of the `quick_insertion_sort` function on the input array.

3. **Test Case Definitions**: Six test cases are defined to evaluate the performance of the `quick_insertion_sort` function.

4. **Setting The Threshold**: The threshold value at which the algorithm switches from Quicksort to Insertion Sort is set to 10.

5. **Executing Test Cases**: The `run_test_case` function is called for each test case, and the execution time is printed to the console.

6. **Output**: The program prints the execution time for each test case, allowing for an analysis of the performance of the Quick-Insertion Sort algorithm under different data conditions.

#### Testing and Benchmarking

Benchmarking results comparing the times of the quick-insertion sort to a traditional quick sort and insertion sort with the same benchmarks.

|                   | Insertion Sort | Quick Sort | Hybrid Sort |
|-------------------|:--------------:|:----------:|:-----------:|
| **1000 Unique**       |   0.018 seconds   | 0.003 seconds | 0.0005 seconds |
| **1000 Reverse Sorted** |   0.036 seconds   | 0.003 seconds | 0.00099 seconds |
| **10000 Unique**      |   1.720 seconds   | 0.038 seconds | 0.0139 seconds |
| **10000 Reverse Sorted** |   3.220 seconds   | 0.036 seconds | 0.0109 seconds |
| **100000 Unique**     | 163.080 seconds | 0.467 seconds | 0.160 seconds |
| **100000 Reverse Sorted** | 319.052 seconds | 0.390 seconds | 0.128 seconds |

---

### Performance Analysis

Transitioning to a local environment from a replit environment eradicated network latency, ensuring more accurate timing results. The only other notable performance issue was setting a recursion limit on the quicksort due to the larger test cases.

---

### Skills Gained

This project helped me gain not only a more in-depth understanding of these algorithms, but also on debugging with memory errors. This let me take a deeper dive in why my code was the way it was and made me research further on my partition function.

---

### Deliverables

Repository: [https://github.com/ThePalad1n/quick-insertion-sort](https://github.com/ThePalad1n/quick-insertion-sort)

---

### Conclusion

The Quick-Insertion Sort algorithm was both challenging and enlightening. It began with a simple yet significant ambition: to accelerate the sorting process by fusing the robustness of Quick Sort with the finesse of Insertion Sort. This endeavor not only aimed at achieving better performance but also served as a deep dive into the intricacies of algorithm design and optimization.

#### Achievements:
- **Algorithm Conception and Design**: Successfully conceptualized and crafted a hybrid algorithm, Quick-Insertion Sort, that dynamically delegates sorting tasks to either Quick Sort or Insertion Sort based on data size and distribution.
- **Code Structure and Implementation**: Built a well-structured and modular code with distinct functions for each algorithm, a partitioning routine, and a mechanism to execute and time test cases.
- **Testing and Benchmarking**: Designed six test cases to rigorously evaluate the performance of the Quick-Insertion Sort against traditional Quick Sort and Insertion Sort.
- **Performance Analysis**: Transitioning to a local environment eradicated network latency, ensuring more accurate timing results.
- **Skills and Knowledge Acquired**: Gained a richer understanding of sorting algorithms, their performance characteristics, and their behavior under different data conditions.

#### Reflections:

The challenges encountered were not mere hurdles but learning stepping stones. The success of the Quick-Insertion Sort algorithm reflects the potential of hybrid algorithms in tackling computational problems more efficiently. This project was an exploration of how blending different algorithmic strategies could lead to more efficient solutions, providing a solid foundation for tackling more complex algorithmic challenges in the future.
