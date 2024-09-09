from sklearn.datasets import fetch_openml

# Import MNIST dataset
mnist = fetch_openml('mnist_784', version=1)

print(mnist.data.iloc[0])