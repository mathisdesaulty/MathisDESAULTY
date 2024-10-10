"""
This module tests the performance of the KNNClassifierMNIST with different metrics.
"""

import time
from Object.k_nn_mnist import KNNClassifierMNIST

TESTS_NUMBER = None
DATASET_SIZE = None
K = None

while DATASET_SIZE is None:
    try:
        DATASET_SIZE = int(input("Enter the size of the dataset: "))
        if DATASET_SIZE <= 0 or DATASET_SIZE > 70000:
            print("Please enter a number between 1 and 70000.")
            DATASET_SIZE = None
    except ValueError:
        print("Please enter a valid number.")

while TESTS_NUMBER is None:
    try:
        TESTS_NUMBER = int(input("Enter the number of tests: "))
        if TESTS_NUMBER <= 0 or TESTS_NUMBER > DATASET_SIZE:
            print(f"Please enter a number between 1 and {DATASET_SIZE}.")
            TESTS_NUMBER = None
    except ValueError:
        print("Please enter a valid number.")

while K is None:
    try:
        K = int(input("Enter the number of neighbors to use: "))
        if K <= 0 or K > DATASET_SIZE:
            print(f"Please enter a number between 1 and {DATASET_SIZE}.")
            K = None
    except ValueError:
        print("Please enter a valid number.")

print("Creating the dataset...")
knn = KNNClassifierMNIST(K, DATASET_SIZE)

# Performance with default metric
print("Starting performance test for default metric...")
start_time = time.time()
performance = knn.performance(TESTS_NUMBER)
end_time = time.time()
print(f"Default metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
      f"Time: {end_time - start_time} seconds")

# Performance with hausdorff_sum metric
print("Starting performance test for hausdorff_sum metric...")
start_time = time.time()
performance = knn.performance(TESTS_NUMBER, "hausdorff_sum")
end_time = time.time()
print(f"Hausdorff_sum metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
      f"Time: {end_time - start_time} seconds")

# Performance with d22 metric
print("Starting performance test for d22 metric...")
start_time = time.time()
performance = knn.performance(TESTS_NUMBER, "d22")
end_time = time.time()
print(f"D22 metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
      f"Time: {end_time - start_time} seconds")

# Performance with d23 metric
print("Starting performance test for d23 metric...")
start_time = time.time()
performance = knn.performance(TESTS_NUMBER, "d23")
end_time = time.time()
print(f"D23 metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
      f"Time: {end_time - start_time} seconds")
