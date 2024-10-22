"""
K-Nearest Neighbors classifier using Hausdorff distance for MNIST dataset.
"""

from collections import Counter
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from Object.math_tool import MathTool
from Object.image_user import ImageUser

class KNNClassifierMNIST:
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
            ImageUser.binarize_image(image.reshape(28, 28)) for image in raw_images.to_numpy()
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

    def _predict(self, x, distance_metric, neighbors_offset=None):
        """
        Predicts the class label for a single data point.
        :param x: Data point to classify.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :param neighbors_offset: Precomputed neighbors offsets for Hausdorff distance.
        :return: Predicted class label.
        """
        # Compute distances between x and all points in the training set
        if neighbors_offset is None:
            neighbors_offset = MathTool.generate_neighbors_offsets(4)
        if distance_metric == 'hausdorff':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance(x, x_train,coords1,
                                                             coords2,neighbors_offset))
        elif distance_metric == 'hausdorff_sum':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance_sum(x, x_train,coords1,
                                                                 coords2, neighbors_offset))
        elif distance_metric == 'd22':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d22(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        elif distance_metric == 'd23':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d23(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        else:
            raise ValueError("Unsupported distance metric")

        # Get the labels of the k nearest neighbors
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [self.labels[i] for i in k_indices]
        # Return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def predict_return_neighbors(self, x, distance_metric='hausdorff', neighbors_offset=None):
        """
        Predicts the class labels for the provided data 
        and returns the indices of the k nearest neighbors.
        :param x: Data to classify.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Predicted class labels and indices of the k nearest neighbors.
        """
        predictions = [
            self._predict_return_neighbors(xi, distance_metric, neighbors_offset) for xi in x
        ]
        return predictions

    def _predict_return_neighbors(self, x, distance_metric, neighbors_offset=None):
        """
        Predicts the class label for a single data point 
        and returns the indices of the k nearest neighbors.
        :param x: Data point to classify.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :param neighbors_offset: Precomputed neighbors offsets for Hausdorff distance.
        :return: Predicted class label and indices of the k nearest neighbors.
        """
        # Compute distances between x and all points in the training set
        if neighbors_offset is None:
            neighbors_offset = MathTool.generate_neighbors_offsets(4)
        if distance_metric == 'hausdorff':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance(x, x_train,coords1,
                                                             coords2,neighbors_offset))
        elif distance_metric == 'hausdorff_sum':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance_sum(x, x_train,coords1,
                                                                 coords2, neighbors_offset))
        elif distance_metric == 'd22':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d22(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        elif distance_metric == 'd23':
            distances = []
            for x_train in self.images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d23(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        else:
            raise ValueError("Unsupported distance metric")

        # Get the labels of the k nearest neighbors
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [self.labels[i] for i in k_indices]

        # Return the most common class label and the indices of the k nearest neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0], k_indices

    def _predict_with_custom_data(
        self, x, images, labels, distance_metric, neighbors_offset=None):
        """
        Predicts the class label for a single data point using a custom dataset.
        :param x: Data point to classify.
        :param images: Custom dataset images.
        :param labels: Custom dataset labels.
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :param neighbors_offset: Precomputed neighbors offsets for Hausdorff distance.
        :return: Predicted class label.
        """
        # Compute distances between x and all points in the custom dataset*
        if neighbors_offset is None:
            neighbors_offset = MathTool.generate_neighbors_offsets(4)
        if distance_metric == 'hausdorff':
            distances = []
            for x_train in images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance(x, x_train,coords1,
                                                             coords2,neighbors_offset))
        elif distance_metric == 'hausdorff_sum':
            distances = []
            for x_train in images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.hausdorff_distance_sum(x, x_train,coords1,
                                                                 coords2, neighbors_offset))
        elif distance_metric == 'd22':
            distances = []
            for x_train in images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d22(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        elif distance_metric == 'd23':
            distances = []
            for x_train in images:
                coords1 = [[i, j] for i in range(len(x))
                           for j in range(len(x[0])) if x[i][j] == 1]
                coords2 = [[i, j] for i in range(len(x_train))
                           for j in range(len(x_train[0])) if x_train[i][j] == 1]
                distances.append(MathTool.distance_d23(x, x_train,coords1,
                                                       coords2, neighbors_offset))
        else:
            raise ValueError("Unsupported distance metric")

        # Get the labels of the k nearest neighbors
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [labels[i] for i in k_indices]

        # Return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


    def performance(self, num_tests=10, distance_metric='hausdorff'):
        """
        Tests the classifier on a subset of the dataset with a separate test set.
        :param num_tests: Number of tests to perform.
        :param test_size: Proportion of data to use for testing (e.g., 0.2 for 20%).
        :param distance_metric: Distance metric to use ('hausdorff' or 'hausdorff_sum').
        :return: Success rate and a tuple of correct and total predictions.
        """
        # Split the dataset into training and test sets
        train_images, test_images, train_labels, test_labels = train_test_split(
            self.images, self.labels, test_size=num_tests/len(self.images), random_state=None)

        print("Test labels:", test_labels)
        correct_predictions = 0
        total_predictions = min(num_tests, len(test_images))

        for i in range(total_predictions):
            image = test_images[i]
            label = test_labels[i]

            # Predict using the training images (not including the test image)
            prediction = self._predict_with_custom_data(
                image, train_images, train_labels, distance_metric)

            if prediction == label:
                correct_predictions += 1

        success_rate = correct_predictions / total_predictions
        return success_rate, (correct_predictions, total_predictions)
