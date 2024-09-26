
from Object.k_nn_mnist import KNNClassifierMINST
import time

knn = KNNClassifierMINST(5,500)

print(len(knn.images))
start_time = time.time()
print(knn.performance(20))
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")

start_time_hausdorff = time.time()
print(knn.performance(20, "hausdorff_sum"))
end_time_hausdorff = time.time()

print(f"Execution time for hausdorff_sum: {end_time_hausdorff - start_time_hausdorff} seconds")

# 500
# (0.95, (19, 20))
# Execution time: 175.33664560317993 seconds
# (0.95, (19, 20))
# Execution time for hausdorff_sum: 226.56142401695251 seconds