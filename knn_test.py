from Object.k_nn_mnist import KNNClassifierMINST

knn = KNNClassifierMINST(5,2000)

print(len(knn.images))

print(knn.test())
