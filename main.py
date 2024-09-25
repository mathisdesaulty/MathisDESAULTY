from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('..')


# Import MNIST dataset
mnist = fetch_openml('mnist_784', version=1)

from Object.image_user import ImageUser
from Object.math_tool import MathTool


n = 1000
image = None
image2 = None
while image is None:
    if mnist.target.iloc[n] == '1':
        image = mnist.data.iloc[n]
    n+=1

while image2 is None:
    n += 1
    if mnist.target.iloc[n] == '1':
        image2 = mnist.data.iloc[n]
    
# to numpyy
image = image.to_numpy().reshape(28, 28)
image2 = image2.to_numpy().reshape(28, 28)
# Binarize the image
binarized_image = ImageUser.binarize_image(image, threshold=128)
# Find coordinates where pixels are equal to 1
binarized_image2 = ImageUser.binarize_image(image2, threshold=128)
print(MathTool.hausdorff_distance(binarized_image, binarized_image2))


# Plot the original and binarized images
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(binarized_image, cmap='gray')
plt.title('binarized_image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(binarized_image2, cmap='gray')
plt.title('binarized_image2')
plt.axis('off') 
plt.suptitle('Hausdorff Distance: {}'.format(MathTool.hausdorff_distance(binarized_image, binarized_image2)))
plt.show()
