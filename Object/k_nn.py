import numpy as np
from collections import Counter
from Object.math_tool import MathTool

class KNNClassifier:
    """
    K-Nearest Neighbors classifier using Hausdorff distance.
    """

    def __init__(self, k=3):
        """
        Initializes the KNN classifier with the number of neighbors to use.
        :param k: Number of neighbors to use for classification.
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        Trains the KNN classifier with training data.
        :param X: Training features.
        :param y: Training labels.
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        Predicts the class labels for the provided data.
        :param X: Data to classify.
        :return: Predicted class labels.
        """
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        """
        Predicts the class label for a single data point.
        :param x: Data point to classify.
        :return: Predicted class label.
        """
        # Compute Hausdorff distances between x and all points in the training set
        distances = [MathTool.hausdorff_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # Return the most common class label among the k neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
