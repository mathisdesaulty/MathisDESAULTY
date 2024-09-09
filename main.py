from sklearn.datasets import fetch_openml
from Object.image_user import ImageUser
import matplotlib.pyplot as plt


# Import MNIST dataset
mnist = fetch_openml('mnist_784', version=1)

imUser = ImageUser()

# Get the first image in the dataset
image = mnist.data.iloc[2]
# to numpyy
image = image.to_numpy().reshape(28, 28)
# Binarize the image
binarized_image = imUser.binarize_image(image, threshold=128)


# Display the binarized image
plt.imshow(binarized_image, cmap='gray')
plt.axis('off')
plt.show()