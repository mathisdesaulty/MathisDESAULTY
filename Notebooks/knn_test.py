
from Object.k_nn_mnist import KNNClassifierMINST

knn = KNNClassifierMINST(5,200)

print(len(knn.images))

print(knn.performance(15))

