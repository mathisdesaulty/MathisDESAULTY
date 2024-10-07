from Object.k_nn_mnist import KNNClassifierMINST
import tkinter as tk
from Object.draw_interface import DrawInterface

if __name__ == "__main__":
    root = tk.Tk()
    interface = DrawInterface(root)
    root.mainloop()

# from Object.k_nn_mnist import KNNClassifierMINST
# import time

# tests_number = 20
# size = 2000
# k = 5

# knn = KNNClassifierMINST(k, size)

# print(f"size of the dataset: {str(len(knn.images))} images for {knn.k} nearest neighbors.")

# # Performance with default metric
# print("Calculating performance with default metric...")
# start_time = time.time()
# performance = knn.performance(tests_number)
# print(f"Performance: {performance[0]}, ratio of correct predictions: {performance[1]}")
# end_time = time.time()
# print(f"Execution time: {end_time - start_time} seconds")

# # Performance with hausdorff_sum metric
# print("Calculating performance with hausdorff_sum metric...")
# start_time_hausdorff = time.time()
# performance = knn.performance(tests_number, "hausdorff_sum")
# print(f"Performance: {performance[0]}, ratio of correct predictions: {performance[1]}")
# end_time_hausdorff = time.time()
# print(f"Execution time for hausdorff_sum: {end_time_hausdorff - start_time_hausdorff} seconds")

# # Performance with d22 metric
# print("Calculating performance with d22 metric...")
# start_time_d22 = time.time()
# performance_d22 = knn.performance(tests_number, "d22")
# print(f"Performance with d22: {performance_d22[0]}, ratio of correct predictions: {performance_d22[1]}")
# end_time_d22 = time.time()
# print(f"Execution time for d22: {end_time_d22 - start_time_d22} seconds")

# # Performance with d23 metric
# print("Calculating performance with d23 metric...")
# start_time_d23 = time.time()
# performance_d23 = knn.performance(tests_number, "d23")
# print(f"Performance with d23: {performance_d23[0]}, ratio of correct predictions: {performance_d23[1]}")
# end_time_d23 = time.time()
# print(f"Execution time for d23: {end_time_d23 - start_time_d23} seconds")