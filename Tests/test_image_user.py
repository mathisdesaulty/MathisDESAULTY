"""
Unit tests for the ImageUser class.

This module contains test cases for the methods of the ImageUser class,
specifically the binarize_image method. The tests cover various scenarios
including normal operation, default thresholds, invalid inputs, and edge cases.
"""

import unittest
import numpy as np
from Object.image_user import ImageUser

class TestImageUser(unittest.TestCase):
    """
    Test cases for the ImageUser class.
    """

    def setUp(self):
        """
        Method executed before each test.
        """

    def test_binarize_image_correct_output(self):
        """
        Test that binarize_image produces the expected output for specific data.
        """
        image = np.array([[100, 150], [200, 50]])
        expected_output = [[0, 1], [1, 0]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

    def test_binarize_image_default_threshold(self):
        """
        Test that binarize_image correctly uses the default threshold.
        """
        image = np.array([[100, 150], [200, 50]])
        expected_output = [[0, 1], [1, 0]]
        result = ImageUser.binarize_image(image)  # Default threshold of 128
        self.assertEqual(result, expected_output)

    def test_binarize_image_invalid_input(self):
        """
        Test that binarize_image raises an exception for an invalid image.
        """
        with self.assertRaises(TypeError):
            ImageUser.binarize_image("invalid_image")

    def test_binarize_image_edge_cases(self):
        """
        Test edge cases for binarize_image.
        """
        # Empty image
        image = np.array([[]])
        expected_output = [[]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

        # Image with all pixels above the threshold
        image = np.array([[255, 255], [255, 255]])
        expected_output = [[1, 1], [1, 1]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

        # Image with all pixels below the threshold
        image = np.array([[0, 0], [0, 0]])
        expected_output = [[0, 0], [0, 0]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
