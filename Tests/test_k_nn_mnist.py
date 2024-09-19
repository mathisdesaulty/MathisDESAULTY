import unittest
from Object.k_nn_mnist import KNNClassifierMINST

class TestKNNClassifierMINST(unittest.TestCase):

    def setUp(self):
        # Initialize the classifier with k=3 and a smaller dataset size for testing
        self.knn = KNNClassifierMINST(k=3, size=100)

    def test_initialization(self):
        # Test if the classifier initializes correctly
        self.assertEqual(len(self.knn.images), 100)
        self.assertEqual(len(self.knn.labels), 100)
        self.assertEqual(self.knn.k, 3)

    def test_predict(self):
        # Test the predict method with a small subset of the data
        test_images = self.knn.images[:10]
        predictions = self.knn.predict(test_images)
        self.assertEqual(len(predictions), 10)
        # Check if predictions are within the valid range of labels
        for prediction in predictions:
            self.assertIn(prediction, range(10))

    def test_test_method(self):
        # Test the test method
        result = self.knn.test(num_tests=10)
        self.assertIsNotNone(result, "The test method returned None")
        success_rate, (correct_predictions, total_predictions) = result
        self.assertGreaterEqual(success_rate, 0)
        self.assertLessEqual(success_rate, 1)
        self.assertEqual(total_predictions, 10)
        self.assertGreaterEqual(correct_predictions, 0)
        self.assertLessEqual(correct_predictions, 10)

if __name__ == '__main__':
    unittest.main()