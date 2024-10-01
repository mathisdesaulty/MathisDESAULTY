
from Object.k_nn_mnist import KNNClassifierMINST
import time

knn = KNNClassifierMINST(5,2000)

print(f"size of the dataset: {str(len(knn.images))} images for {knn.k} nearest neighbors.")
start_time = time.time()
performance = knn.performance(10)
print(f"Performance: {performance[0]}, ratio of correct predictions: {performance[1]}")
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")

start_time_hausdorff = time.time()
performance = knn.performance(10, "hausdorff_sum")
print(f"Performance: {performance[0]}, ratio of correct predictions: {performance[1]}")

end_time_hausdorff = time.time()

print(f"Execution time for hausdorff_sum: {end_time_hausdorff - start_time_hausdorff} seconds")