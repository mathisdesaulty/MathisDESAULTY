"""
Unit tests for the KNNClassifierMINST class.
"""
import unittest
from Object.k_nn_mnist import KNNClassifierMINST

class TestKNNClassifierMINST(unittest.TestCase):
    """Unit tests for the KNNClassifierMINST class."""

    def setUp(self):
        """Set up the KNN classifier with k=3 and a smaller dataset size for testing."""
        self.knn = KNNClassifierMINST(k=3, size=100)

    def test_initialization(self):
        """Test if the classifier initializes correctly with the given parameters."""
        self.assertEqual(len(self.knn.images), 100, "The number of images should be 100.")
        self.assertEqual(len(self.knn.labels), 100, "The number of labels should be 100.")
        self.assertEqual(self.knn.k, 3, "The value of k should be 3.")

    def test_predict(self):
        """Test the predict method with a small subset of the data (first 10 images)."""
        test_images = self.knn.images[:10]
        predictions = self.knn.predict(test_images)
        self.assertEqual(len(predictions), 10, "The number of predictions should be 10.")
        # Check if predictions are within the valid range of labels (0-9)
        for prediction in predictions:
            self.assertIn(prediction, range(10), "Each prediction should be in the range 0-9.")

    def test_predict_hausdorff_sum(self):
        """Test the predict method using the Hausdorff sum distance 
        metric with a small subset of the data (first 10 images)."""
        test_images = self.knn.images[:10]
        predictions = self.knn.predict(test_images, distance_metric='hausdorff_sum')
        self.assertEqual(len(predictions), 10, "The number of predictions should be 10.")
        # Check if predictions are within the valid range of labels (0-9)
        for prediction in predictions:
            self.assertIn(prediction, range(10), "Each prediction should be in the range 0-9.")

    def test_performance_method(self):
        """Test the performance method with a small number of tests (10)."""
        result = self.knn.performance(num_tests=10)
        self.assertIsNotNone(result, "The performance method should not return None.")
        success_rate, (correct_predictions, total_predictions) = result
        self.assertGreaterEqual(success_rate, 0, "The success rate should be at least 0.")
        self.assertLessEqual(success_rate, 1, "The success rate should be at most 1.")
        self.assertEqual(total_predictions, 10, "The total number of predictions should be 10.")
        self.assertGreaterEqual(correct_predictions, 0, 
                                "The number of correct predictions should be at least 0.")
        self.assertLessEqual(correct_predictions, 10, 
                             "The number of correct predictions should be at most 10.")

    def test_performance_method_hausdorff_sum(self):
        """Test the performance method using the Hausdorff sum distance metric
        with a small number of tests (10)."""
        result = self.knn.performance(num_tests=10, distance_metric='hausdorff_sum')
        self.assertIsNotNone(result, "The performance method should not return None.")
        success_rate, (correct_predictions, total_predictions) = result
        self.assertGreaterEqual(success_rate, 0, "The success rate should be at least 0.")
        self.assertLessEqual(success_rate, 1, "The success rate should be at most 1.")
        self.assertEqual(total_predictions, 10, "The total number of predictions should be 10.")
        self.assertGreaterEqual(correct_predictions, 0, 
                                "The number of correct predictions should be at least 0.")
        self.assertLessEqual(correct_predictions, 10, 
                             "The number of correct predictions should be at most 10.")

if __name__ == '__main__':
    unittest.main()
