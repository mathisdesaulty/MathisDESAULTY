# Specification Document

# Langages

For this project, I plan to use the Python programming language. It's one of the high-level languages that will enable me to set up this project in the best possible conditions. As for the languages that I know and can correct, Python, C and Java are languages that I've mastered and that I'll be able to work on during the reviews.

# The implemented data structures and algorithms

The data structures I plan to use for this project are arrays to store images, distances and labels. For pixel manipulation, I plan to use numpy arrays to create matrices to represent the images. To finish with the data structures, I think it would be interesting to use dictionaries to link the images with their labels, i.e. their numbers.

As far as the algorithm used is concerned, I'm going to start by converting the images to greyscale and then use the k-nearest neighbours. As for the distance formula used, I think we need to test it to see which is the best, in particular the Hausdorff Distance and the D23 measure.

# Problem solved

The problem solved by this project is the recognition of handwritten digits using the k-nn algorithm. This recognition breaks down into several different problems: transforming the images into a black and white matrix so that they can be compared with each other, then comparing the different images and choosing the distance.

# Input used by the program and its use

The knn algorithm therefore takes as input images that will have to be transformed to the correct size by having only black and white pixels. It then compares the distances between these images using specific distances. 

# Desired time complexity

In terms of complexity time, for data storage the complexity time is O(1) because there is no calculation to be done, but for the prediction complexity time we have O(n.d) where n is the number of examples in the dataset and d is the size of each of the elements. If we use the MNIST dataset made up of 60,000 images that we will convert into 28.28 pixels, then O(60000.784).
In terms of space complexity, the only thing we need to take into account is the data set, which in this case is 60,000, so we'll also have a complexity of O(nxd), which we can calculate if we keep a single byte for each pixel: 
60000×784=47040000 octets ≈ 47 Mo.

The k-nn algorithm is not particularly fast in itself, as we can see from the following completion time

# References

[https://github.com/shilparai/image_classification_knn](https://github.com/shilparai/image_classification_knn)

[kNN for image classification](https://www.youtube.com/watch?v=lGh_zCyY7TY)

[Convert an image to a black and white image in python](https://www.youtube.com/watch?v=TYcV2iy7MP8)
