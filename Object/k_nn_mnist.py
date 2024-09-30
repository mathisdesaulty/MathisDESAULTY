"""
K-Nearest Neighbors classifier using Hausdorff distance for MNIST dataset.
"""

from collections import Counter
from sklearn.datasets import fetch_openml
from Object.math_tool import MathTool
from Object.image_user import ImageUser

class KNNClassifierMINST:
    """
    K-Nearest Neighbors classifier using Hausdorff distance.
    """

    def __init__(self, k, size=1000):
        """
        Initializes the KNN classifier with the number of neighbors to use.
        :param k: Number of neighbors to use for classification.
        :param size: Number of elements to use from the MNIST dataset.
        """
        data = fetch_openml('mnist_784', version=1)
        raw_images = data['data'][:size]
        self.images = [
            ImageUser.binarize_image(image.reshape(28,28)) for image in raw_images.to_numpy()
        ]
        self.labels = data['target'][:size].astype(int).tolist()
        self.k = k

    def predict(self, x, distance_metric='hausdorff'):
        """
        Predicts the class labels for the provided data.
        :param x: Data to classify.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Predicted class labels.
        """
        predictions = [self._predict(xi, distance_metric) for xi in x]
        return predictions

    def _predict(self, x, distance_metric):
        """
        Predicts the class label for a single data point.
        :param x: Data point to classify.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Predicted class label.
        """
        # Compute distances between x and all points in the training set
        if distance_metric == 'hausdorff':
            distances = [
                MathTool.hausdorff_distance(x, x_train) for x_train in self.images
            ]
        elif distance_metric == 'hausdorff_sum':
            distances = [
                MathTool.hausdorff_distance_sum(x, x_train) for x_train in self.images
            ]
        else:
            raise ValueError("Unsupported distance metric")

        # Get the labels of the k nearest neighbors
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [self.labels[i] for i in k_indices]

        # Return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def _predict_with_custom_data(self, x, images, labels, distance_metric):
        """
        Predicts the class label for a single data point using a custom dataset.
        :param x: Data point to classify.
        :param images: Custom dataset images.
        :param labels: Custom dataset labels.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Predicted class label.
        """
        # Compute distances between x and all points in the custom dataset
        if distance_metric == 'hausdorff':
            distances = [MathTool.hausdorff_distance(x, x_train) for x_train in images]
        elif distance_metric == 'hausdorff_sum':
            distances = [MathTool.hausdorff_distance_sum(x, x_train) for x_train in images]
        else:
            raise ValueError("Unsupported distance metric")

        # Get the labels of the k nearest neighbors
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [labels[i] for i in k_indices]

        # Return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def performance(self, num_tests=100, distance_metric='hausdorff'):
        """
        Tests the classifier on a subset of the dataset.
        :param num_tests: Number of tests to perform.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Success rate and a tuple of correct and total predictions.
        """
        correct_predictions = 0
        total_predictions = min(num_tests, len(self.images))

        for i in range(total_predictions):
            image = self.images[i]
            label = self.labels[i]
            # Exclude the current image from the training set
            other_images = self.images[:i] + self.images[i + 1:]
            other_labels = self.labels[:i] + self.labels[i + 1:]

            # Predict using the remaining images
            prediction = self._predict_with_custom_data(
                image, other_images, other_labels, distance_metric)
            if prediction == label:
                correct_predictions += 1

        success_rate = correct_predictions / total_predictions
        return success_rate, (correct_predictions, total_predictions)
